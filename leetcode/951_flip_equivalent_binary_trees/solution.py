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

    def __repr__(self) -> str:
        return f'<TreeNode val={self.val}, left={self.left}, right={self.right}>'


class Solution:
    def construct_dict(self, root: TreeNode) -> dict:
        level_dict = dict()
        if root is None:
            return level_dict
        level = 1
        cur_level = list()
        next_level = list()
        cur_level.append(root)
        while len(cur_level) > 0:
            cur_node = cur_level.pop(0)
            if level not in level_dict:
                level_dict[level] = list()
            child_vals = list()
            if cur_node.left is not None:
                child_vals.append(cur_node.left.val)
                next_level.append(cur_node.left)
            if cur_node.right is not None:
                child_vals.append(cur_node.right.val)
                next_level.append(cur_node.right)
            level_dict[level].append(tuple([cur_node.val, set(child_vals)]))
            if len(cur_level) == 0 and len(next_level) > 0:
                cur_level = next_level
                next_level = list()
                level += 1

        for i in range(1, level+1):
            # print(level_dict[i])
            level_dict[i] = sorted(level_dict[i], key=lambda x: x[0])
        # print(level_dict)
        return level_dict

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        dict1 = self.construct_dict(root1)
        dict2 = self.construct_dict(root2)
        return dict1 == dict2


    def construct_tree(self, nodes: List[int]) -> TreeNode:
        root = None
        prev_level = list()
        cur_level = list()
        level = 1
        added = 0
        for idx, n in enumerate(nodes):
            # print(f'idx: {idx}, n: {n}')
            if idx == 0:
                node = TreeNode(val=n)
                root = node
                prev_level.append(node)
                level += 1
                continue
            
            if idx == (2**level)-1:
                prev_level = cur_level
                cur_level = list()
                level += 1
            
            # print(f'    level: {level}, cur_level: {cur_level}, prev_level: {prev_level}')
            
            if n is None:
                cur_node = None
            else:
                cur_node = TreeNode(val=n)
            cur_level.append(cur_node)

            if added == 0:
                parent_node = prev_level.pop(0)
                if parent_node is not None:
                    parent_node.left = cur_node
            else:
                if parent_node is not None:
                    parent_node.right = cur_node
            added = (added+1)%2
        print(root)
        return root


    def solve(self, nodes1: List[int], nodes2: List[int]) -> bool:
        root1 = self.construct_tree(nodes1)
        root2 = self.construct_tree(nodes2)
        # print(f'root1: {root1}')
        return self.flipEquiv(root1, root2)
        


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,3,4,5,6,None,None,None,7,8], [1,3,2,None,6,4,5,None,None,None,None,8,7]], True),
        ([[], []], True),
        ([[], [1]], False),
        ([[0,None,1], [0,1]], True),
    ]

    Tester.factory(test_cases, func=lambda input: sol.solve(*input)).run(unordered_output=False)
