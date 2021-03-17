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
    def productExceptSelf(self, nums: List[int]) -> List[int]: # no division
        length = len(nums)
        left, right = [1] * length, [1] * length

        l_base = 1
        for i in range(length):
            if i == 0:
                left[i] = l_base
            else:
                l_base *= nums[i-1]
                left[i] = l_base
        
        r_base = 1
        for i in range(length-1, -1, -1):
            if i == length-1:
                right[i] = r_base
            else:
                r_base *= nums[i+1]
                right[i] = r_base

        return [left[i] * right[i] for i in range(length)]


    def productExceptSelf_usingDiv(self, nums: List[int]) -> List[int]:
        all_product = 1
        zero_count = 0
        zero_idx = list()
        for idx, num in enumerate(nums):
            all_product *= num
            if num == 0:
                zero_count += 1
                zero_idx.append(idx)

        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            except_product = 1
            for num in nums:
                if num != 0:
                    except_product *= num
            ans = [0] * len(nums)
            ans[zero_idx[0]] = except_product
            return ans
        else:
            ans = list()
            for num in nums:
                ans.append(all_product // num)
            return ans


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,3,4]], [24,12,8,6]),
        ([[-1,1,0,-3,3]], [0,0,9,0,0]),
        ([[-1,1,0,-3,3,0]], [0,0,0,0,0,0]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.productExceptSelf(*input)).run(unordered_output=False)
