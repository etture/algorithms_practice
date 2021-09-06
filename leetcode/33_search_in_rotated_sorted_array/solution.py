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
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        pivot = self.find_pivot(nums)
        # print(f'pivot: {pivot}')

        left_section = nums[:pivot+1]
        right_section = nums[pivot+1:]
        # print(f'left: {left_section}, right: {right_section}')

        if nums[0] <= target:
            to_search = left_section
            idx_add_factor = 0
        else:
            to_search = right_section
            idx_add_factor = len(left_section)
        # print(f'to_search: {to_search}, add_factor: {idx_add_factor}')

        left, right = 0, len(to_search) - 1
        while True:
            middle = (left + right) // 2
            # print(f'left: {left}, right: {right}, middle: {middle}')
            if right < left:
                return -1
            if to_search[middle] == target:
                return middle + idx_add_factor
            elif to_search[middle] < target:
                left = middle + 1
            else:
                right = middle - 1


    def find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while True:
            middle = (left + right) // 2
            if middle == len(nums)-1:
                return middle
            if nums[middle] > nums[middle+1]:
                return middle
            elif nums[left] > nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[4,5,6,7,0,1,2],0], 4),
        ([[4,5,6,7,0,1,2],3], -1),
        ([[0,1,2,4,5,6,7],0], 0),
        ([[7,0,1,2,4,5,6],0], 1),
        ([[1],0], -1),
        ([[1,3],2], -1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.search(*input)).run(unordered_output=False)
