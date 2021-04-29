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
# ----------------------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'<val: {self.val}, left: {self.left}, right: {self.right}>'


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None: return 0
        diameter = 0
        def max_depth(node: TreeNode):
            if node is None: return 0
            left_path = max_depth(node.left)
            right_path = max_depth(node.right)
            nonlocal diameter
            diameter = max(diameter, left_path + right_path)
            print(f'diameter: {diameter}')
            return max(left_path, right_path) + 1
        max_depth(root)
        return diameter


class Problem:
    def solve(self, nodes: List[int]) -> int:
        sol = Solution()
        if len(nodes) == 0:
            return sol.diameterOfBinaryTree(None)
        else:
            head = None
            cur_level, next_level = list(), list()
            for idx, node in enumerate(nodes):
                if idx == 0:
                    head = TreeNode(val=node)
                    cur_level.append(head)
                else:
                    cur_node = TreeNode(val=node)
                    next_level.append(cur_node)
                    if cur_level[0].left is None:
                        cur_level[0].left = cur_node
                    elif cur_level[0].right is None:
                        cur_level[0].right = cur_node
                        cur_level.pop(0)
                        if len(cur_level) == 0:
                            cur_level = next_level
                            next_level = list()
            # print(head)
            return sol.diameterOfBinaryTree(head)





if __name__ == '__main__':
    test_cases = [
        ([[1,2,3,4,5]], 3),
        ([[1,2]], 1),
        ([[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]], 8)
    ]
    prob = Problem()
    Tester.factory(test_cases, func=lambda input: prob.solve(*input)).run(unordered_output=False)
