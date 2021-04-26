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
        if len(nums) < 3: return []

        two_sets = dict()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                two_sets[(i, j)] = (nums[i]+nums[j], (nums[i], nums[j]))
        
        # print(two_sets)
        answer = list()
        for idx, num in enumerate(nums):
            for key in two_sets.keys():
                if idx not in key and two_sets[key][0] == -num:
                    match = list(two_sets[key][1])
                    match.append(num)
                    match = sorted(match)
                    if match not in answer:
                        # print(f'idx: {idx}, num: {num}, key: {key}, two_sets[key]: {two_sets[key]}')
                        answer.append(match)
        return answer
                    
        
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[-1,0,1,2,-1,-4]], [[-1,-1,2],[-1,0,1]]),
        ([[]], []),
        ([[0]], []),
    ]

    Tester.factory(test_cases, func=lambda input: sol.threeSum(*input)).run(unordered_output=True)
