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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.global_answer = list()

        if root is None: return []
        self.traverse(root)
        return self.global_answer
    
    def traverse(self, node: Optional[TreeNode]):
        if node is not None:
            self.traverse(node.left)
            self.global_answer.append(node.val)
            self.traverse(node.right)


class Helper:
    def run(self, _input: List[int]) -> List[int]:
        root_node = None
        prev_level_nodes = list()
        cur_level_nodes = list()

        idx = 0
        left_filled = False
        while idx < len(_input):
            print(f'idx: {idx}, prev: {prev_level_nodes}, cur: {cur_level_nodes}')
            val = _input[idx]
            if idx == 0:
                root_node = TreeNode(val)
                prev_level_nodes.append(root_node)
                idx += 1
            elif len(prev_level_nodes) == 0:
                prev_level_nodes = cur_level_nodes
                cur_level_nodes = list()
                left_filled = False
            else:
                node = TreeNode(val) if val is not None else None
                if not left_filled:
                    prev_level_nodes[0].left = node
                    left_filled = True
                else:
                    prev_level_nodes[0].right = node
                    prev_level_nodes.pop(0)
                    left_filled = False
                if node is not None:
                    cur_level_nodes.append(node)
                idx += 1
        
        sol = Solution()
        return sol.inorderTraversal(root_node)    


if __name__ == '__main__':
    sol = Helper()

    test_cases = [
        ([[1,None,2,3]], [1,3,2]),
        ([[]], []),
        ([[1]], [1]),
        ([[1,2]], [2,1]),
        ([[1,None,2]], [1,2]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.run(*input)).run(unordered_output=False)
