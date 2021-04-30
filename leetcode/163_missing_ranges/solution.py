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
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        answer = list()

        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [f'{lower}->{upper}']

        cur_min = lower
        for idx, num in enumerate(nums):
            if num == cur_min:
                cur_min = num + 1
            else:
                range_end = num - 1
                if cur_min == range_end:
                    answer.append(str(cur_min))
                else:
                    answer.append(f'{cur_min}->{range_end}')
                cur_min = num + 1
        if nums[-1] < upper:
            if nums[-1] + 1 == upper:
                answer.append(str(upper))
            else:
                answer.append(f'{nums[-1]+1}->{upper}')
        return answer



        # cur_missing_range = list()
        # for i in range(lower, upper + 1):
        #     if i not in nums:
        #         cur_missing_range.append(i)
        #     elif len(cur_missing_range) > 0:
        #         if len(cur_missing_range) == 1:
        #             answer.append(str(cur_missing_range[0]))
        #         else:
        #             answer.append(f'{cur_missing_range[0]}->{cur_missing_range[-1]}')
        #         cur_missing_range = list()
        # if len(cur_missing_range) > 0:
        #     if len(cur_missing_range) == 1:
        #         answer.append(str(cur_missing_range[0]))
        #     else:
        #         answer.append(f'{cur_missing_range[0]}->{cur_missing_range[-1]}')
        # return answer



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[0,1,3,50,75], 0, 99], ["2","4->49","51->74","76->99"]),
        ([[], 1, 1], ["1"]),
        ([[], -3, -1], ["-3->-1"]),
        ([[-1], -1, -1], []),
        ([[-1], -2, -1], ["-2"]),
        ([[1000000000], 0, 1000000000], ["0->999999999"]),
        ([[-1], -1, 0], ["0"]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.findMissingRanges(*input)).run(unordered_output=False)
