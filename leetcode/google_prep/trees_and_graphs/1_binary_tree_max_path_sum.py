# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 

sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=True)                             
# ----------------------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        class UniversalMax:
            def __init__(self, val=-99999999):
                self.val = val

            def set_max(self, max_val):
                if max_val > self.val:
                    self.val = max_val

        def recursively_find_max(treenode: TreeNode, umax) -> int:
            me = treenode.val
            left_max, right_max = 0, 0
            if treenode.left:
                left_max = recursively_find_max(treenode.left, umax)
            if treenode.right:
                right_max = recursively_find_max(treenode.right, umax)

            max_group = [me, me+left_max, me+right_max, me+left_max+right_max]
            if treenode.left:
                max_group.extend([left_max])
            if treenode.right:
                max_group.extend([right_max])

            local_max = max(max_group)
            umax.set_max(local_max)
            global_max = max(me, me+left_max, me+right_max)
            print(f'me: {me}, left_max: {left_max}, right_max: {right_max}, max_val: {umax.val}')
            return global_max
        
        univ_max = UniversalMax()
        recursively_find_max(root, univ_max)
        return univ_max.val



    def constructTree(self, tree) -> int:
        root_node = None
        nodes = list()
        for idx, val in enumerate(tree):
            # print(f'idx: {idx}, val: {val}')
            if val:
                node = TreeNode(val=val)
                nodes.append(node)
                if idx == 0:
                    root_node = node
                else:
                    parent_node = nodes[(idx-1)//2]
                    if idx % 2 == 1:
                        parent_node.left = node
                    else:
                        parent_node.right = node
        
        return self.maxPathSum(root_node)



'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    ([[1,2,3]], 6),
    ([[-10,9,20,None,None,15,7]], 42),
    ([[-3]], -3),
    ([[5,4,8,11,None,13,4,7,2,None,None,None,1]], 48)
]

# 0 1 2 3 4 5 6
# 3,4 == (2*1) + 1, 2
# 5,6 == (2*2) + 1, 2
# 7,8 == (2*3) + 1,2
# 9,10

solution = Solution().constructTree

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
