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
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        if length == 2: return max(nums)

        self.nums = nums
        self.memo = dict()
        return max(self.calc(nums[:-1]), self.calc(nums[1:]))

    def calc(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        temp = [0] * len(nums)
        for idx, num in enumerate(nums):
            if idx < 2: 
                temp[idx] = num
            elif idx == 2:
                temp[idx] = num + temp[0]
            else:
                temp[idx] = num + max(temp[idx-2], temp[idx-3])
        # print(f'temp: {temp}')
        return max(temp[-1], temp[-2])


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[2,3,2]], 3),
        ([[1,2,3,1]], 4),
        ([[1,2,3]], 3),
        ([[1,2,3,4,5,6,7]], 15),
        ([[]], 0),
        ([[199]], 199),
        ([[1,3,1,3,100]], 103),
        ([[2,1,1,2]], 3),
        ([[2,2,4,3,2,5]], 10),
        ([[200,3,140,20,10]], 340),
    ]

    Tester.factory(test_cases, func=lambda input: sol.rob(*input)).run(unordered_output=False)
