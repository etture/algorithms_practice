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

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        fruit_types = dict()
        max_cnt = 0
        cur_cnt = 0
        for idx, fruit in enumerate(tree):
            if len(fruit_types) < 2:
                if fruit not in fruit_types:
                    fruit_types[fruit] = 1
                cur_cnt += 1
                max_cnt = max(cur_cnt, max_cnt)
            elif fruit in fruit_types:
                if fruit != tree[idx-1]:
                    fruit_types[fruit] = 0
                fruit_types[fruit] += 1
                cur_cnt += 1
                max_cnt = max(cur_cnt, max_cnt)
            else:
                fruits_in_basket = list(fruit_types.keys())
                fruit_to_evict = fruits_in_basket[0] if tree[idx-1] == fruits_in_basket[1] else fruits_in_basket[1]
                del fruit_types[fruit_to_evict]
                fruit_types[fruit] = 1
                cur_cnt = sum([v for v in fruit_types.values()])
                max_cnt = max(cur_cnt, max_cnt)
        return max_cnt



test_cases = [
    ([[1,2,1]], 3),
    ([[0,1,2,2]], 3),
    ([[1,2,3,2,2]], 4),
    ([[3,3,3,1,2,1,1,2,3,3,4]], 5),
    ([[0,0,1,1]], 4),
    ([[0,1,6,6,4,4,6]], 5),
]


if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.totalFruit(*input)).run(unordered_output=False)
