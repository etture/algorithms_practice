# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 

sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=True)                             
# ----------------------------------------------------------

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2
        even = total_len % 2 == 0
        if even: # even
            stop_point = (total_len // 2) + 1
        else: # odd
            stop_point = (total_len + 1) // 2
        cnt = 0
        prev_num, cur_num = -999, -999
        while cnt < stop_point:
            cnt += 1
            prev_num = cur_num
            if len(nums1) == 0:
                cur_num = nums2.pop(0)
            elif len(nums2) == 0:
                cur_num = nums1.pop(0)
            elif nums1[0] < nums2[0]:
                cur_num = nums1.pop(0)
            else:
                cur_num = nums2.pop(0)
        if even:
            return (prev_num + cur_num) / 2
        else:
            return cur_num




'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    ([[1,3],[2]], 2.0),
    ([[1,2], [3,4]], 2.5)
]



solution = Solution().findMedianSortedArrays

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
