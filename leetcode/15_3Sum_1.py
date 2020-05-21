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
# ----------------------------------------------------------

from typing import List
import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinations = itertools.combinations(nums, 3)
        answers = set()
        redundant_combs = set()
        for cmb in combinations:
            cmb = tuple(sorted(cmb))
            if cmb in redundant_combs:
                continue
            redundant_combs.add(cmb)
            if sum(cmb) == 0:
                answers.add(cmb)
        return [list(a) for a in answers]


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    (
        [[-1, 0, 1, 2, -1, -4]],
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
    ),
    (
        [[-7,-11,12,-15,14,4,4,11,-11,2,-8,5,8,14,0,3,2,3,-3,-15,-2,3,6,1,2,8,-5,-7,3,1,8,11,-3,6,3,-4,-13,-15,14,-8,2,-8,4,-13,13,11,5,0,0,9,-8,5,-2,14,-9,-15,-1,-6,-15,9,10,9,-2,-8,-8,-14,-5,-14,-14,-6,-15,-5,-7,5,-11,14,-7,2,-9,0,-4,-1,-9,9,-10,-11,1,-4,-2,2,-9,-15,-12,-4,-8,-5,-11,-6,-4,-9,-4,-3,-7,4,9,-2,-5,-13,7,2,-5,-12,-14,1,13,-9,-3,-9,2,3,8,0,3]],
        [
            'something'
        ]
    )
]

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: Solution().threeSum(input[0])
    ).run(unordered_output=True)