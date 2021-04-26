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
        if len(tree) == 0: return 0
        if len(tree) == 1: return 1
        baskets = dict()
        max_count, cur_count = 0, 0
        for idx, fruit in enumerate(tree):
            if fruit in baskets:
                if idx - 1 >= 0 and tree[idx-1] == fruit:
                    baskets[fruit]['consecutive'] += 1
                else:
                    baskets[fruit]['consecutive'] = 1
                baskets[fruit]['count'] += 1
                cur_count += 1
            elif len(baskets) < 2:
                baskets[fruit] = {
                    'count': 1,
                    'consecutive': 1
                }
                cur_count += 1
            else:
                prev_fruit = tree[idx-1]
                baskets = {
                    prev_fruit: {
                        'count': baskets[prev_fruit]['consecutive'],
                        'consecutive': baskets[prev_fruit]['consecutive']
                    },
                    fruit: {
                        'count': 1,
                        'consecutive': 1
                    }
                }
                cur_count = baskets[prev_fruit]['count'] + 1
            # print(f'idx: {idx}, fruit: {fruit}, baskets: {baskets}')
            max_count = max(max_count, cur_count)
        return max_count
            




test_cases = [
    ([[1,2,1]], 3),
    ([[0,1,2,2]], 3),
    ([[1,2,3,2,2]], 4),
    ([[3,3,3,1,2,1,1,2,3,3,4]], 5),
    ([[0,0,1,1]], 4),
    ([[0,1,6,6,4,4,6]], 5),
    ([[1,0,1,4,1,4,1,2,3]], 5),
]


if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.totalFruit(*input)).run(unordered_output=False)
