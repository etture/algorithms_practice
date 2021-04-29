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
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_nums = len(nums1) + len(nums2)
        is_even = (total_nums) % 2 == 0
        combined = list()
        counter = 0
        while len(nums1) > 0 or len(nums2) > 0:
            if len(nums2) == 0:
                combined.append(nums1.pop(0))
            elif len(nums1) == 0:
                combined.append(nums2.pop(0))
            elif nums1[0] >= nums2[0]:
                combined.append(nums2.pop(0))
            elif nums2[0] > nums1[0]:
                combined.append(nums1.pop(0))
            counter += 1
            if counter == (total_nums // 2) + 1:
                break
        if is_even:
            return (combined[-1] + combined[-2]) / 2
        else:
            return combined[-1]
                

            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,3],[2]], 2.0),
        ([[1,2],[3,4]], 2.5),
        ([[0,0],[0,0]], 0.0),
        ([[2],[]], 2.0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.findMedianSortedArrays(*input)).run(unordered_output=False)
