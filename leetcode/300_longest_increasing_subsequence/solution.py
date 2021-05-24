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
    def lengthOfLIS(self, nums: List[int]) -> int:
        decks = list()
        for num in nums:
            if len(decks) == 0:
                decks.append(num)
            else:
                left, right = 0, len(decks) - 1
                insert_idx = -1
                while left <= right:
                    middle = (left + right) // 2
                    if decks[middle] >= num:
                        insert_idx = middle
                        right = middle - 1
                    else:
                        left = middle + 1
                if insert_idx < 0:
                    decks.append(num)
                else:
                    decks[insert_idx] = num
        # print(decks)
        return len(decks)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[10,9,2,5,3,7,101,18]], 4),
        ([[0,1,0,3,2,3]], 4),
        ([[7,7,7,7,7,7,7]], 1),
        ([[4,10,4,3,8,9]], 3),
    ]

    Tester.factory(test_cases, func=lambda input: sol.lengthOfLIS(*input)).run(unordered_output=False)
