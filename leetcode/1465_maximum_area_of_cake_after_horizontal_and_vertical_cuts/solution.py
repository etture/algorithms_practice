# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 
# 파이썬 기본 재귀 limit이 1000이라고 함 --> 10^6으로 manual하게 설정
sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=False)                             
import pprint
pp = pprint.PrettyPrinter()
# ----------------------------------------------------------

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        max_h, max_v = 0, 0
        for idx, h_cut in enumerate(horizontalCuts):
            # print(f'h_cut: {h_cut}')
            if idx == 0:
                max_h = max(max_h, h_cut)
            else:
                max_h = max(max_h, h_cut - horizontalCuts[idx-1])
            #     print(f'h_cut: {h_cut}, horizontalCuts[idx-1]: {horizontalCuts[idx-1]}, diff: {h_cut - horizontalCuts[idx-1]}')
            # print(f'max_h: {max_h}')
        max_h = max(max_h, h - horizontalCuts[-1])

        for idx, v_cut in enumerate(verticalCuts):
            if idx == 0:
                max_v = max(max_v, v_cut)
            else:
                max_v = max(max_v, v_cut - verticalCuts[idx-1])
            #     print(f'v_cut: {v_cut}, verticalCuts[idx-1]: {verticalCuts[idx-1]}, diff: {v_cut - verticalCuts[idx-1]}')
            # print(f'max_v: {max_v}')
        max_v = max(max_v, w - verticalCuts[-1])
        # print(f'max_v: {max_v}')

        return (max_h * max_v) % (10**9 + 7)




    class Node:
        def __init__(self, h: int, w: int):
            self.coord = (h, w)
            self.right = None
            self.down = None

        def __repr__(self) -> str:
            return f'<Node coord: {self.coord}, right; {self.right.coord if self.right else self.right}, down: {self.down.coord if self.down else self.down}>'

        def count_connected(self, visited: set(tuple)) -> int:
            if self.coord in visited: return 0
            visited.add(self.coord)
            right = self.right.count_connected(visited) if self.right else 0
            down = self.down.count_connected(visited) if self.down else 0
            return right + down + 1


    def maxArea_graph(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # construct cake graph
        cake = list()
        for h_idx in range(h):
            row = list()
            for w_idx in range(w):
                node = self.Node(h_idx, w_idx)
                if h_idx > 0:
                    cake[h_idx-1][w_idx].down = node
                if w_idx > 0:
                    row[-1].right = node
                row.append(node)
            cake.append(row)
        
        # print(cake)

        for h_cut in horizontalCuts:
            for node in cake[h_cut-1]:
                node.down = None

        for v_cut in verticalCuts:
            for node in [row[v_cut-1] for row in cake]:
                node.right = None

        # print(cake)
        visited = set()
        max_area = 0
        for h_idx in range(h):
            for w_idx in range(w):
                max_area = max(max_area, cake[h_idx][w_idx].count_connected(visited))
        return max_area % ((10**9)+7)
            



        
            



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([5,4,[1,2,4],[1,3]], 4),
        ([5,4,[3,1],[1]], 6),
        ([5,4,[3],[3]], 9),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maxArea(*input)).run(unordered_output=False)
