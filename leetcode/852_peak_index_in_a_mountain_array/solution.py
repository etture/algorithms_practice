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
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Linear
        # max_val = -1
        # max_idx = -1
        # for idx, elem in enumerate(arr):
        #     if elem > max_val:
        #         max_val = elem
        #         max_idx = idx
        # return max_idx

        # Binary Search
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            print(f'left: {left}, right: {right}, mid: {mid}')
            # if mid == 0:
            #     return 0
            # elif mid == len(arr) - 1:
            #     return len(arr) - 1
            # else:
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                right = mid
            else:
                left = mid



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[0,1,0]], 1),
        ([[0,2,1,0]], 1),
        ([[0,10,5,2]], 1),
        ([[0,10,15,2]], 2),
        ([[20,10,5,2]], 0),
        ([[3,5,3,2,0]], 1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.peakIndexInMountainArray(*input)).run(unordered_output=False)
