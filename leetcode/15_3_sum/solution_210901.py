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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        USED = True
        answers = set()
        for i in range(len(nums)-2):
            pivot = nums[i]
            target = 0 - pivot
            hashmap = dict()
            for j in range(i+1, len(nums)):
                if j == i+1:
                    hashmap[nums[j]] = not USED
                else:
                    complement = target - nums[j]
                    if complement in hashmap and hashmap[complement] is not USED:
                        hashmap[complement] = USED
                        hashmap[nums[j]] = USED
                        answers.add(tuple(sorted([pivot, complement, nums[j]])))
                    elif nums[j] not in hashmap:
                        hashmap[nums[j]] = not USED
        return [list(a) for a in answers]
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[-1,0,1,2,-1,-4]], [[-1,-1,2],[-1,0,1]]),
        ([[]], []),
        ([[0]], []),
    ]

    Tester.factory(test_cases, func=lambda input: sol.threeSum(*input)).run(unordered_output=True)
