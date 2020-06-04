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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        lower_lim, upper_lim = 0, length - 1
        search_idx = (lower_lim + upper_lim) // 2

        start_pos, end_pos = -1, -1

        # find target
        target_idx = -1
        while lower_lim <= upper_lim:
            query = nums[search_idx]
            print(f'search_idx: {search_idx}, query: {query}, target: {target} (lower_lim: {lower_lim}, upper_lim: {upper_lim})')
            if query > target:
                upper_lim = search_idx - 1
                search_idx = (lower_lim + upper_lim) // 2
            elif query < target:
                lower_lim = search_idx + 1
                search_idx = (lower_lim + upper_lim) // 2
            else: # match
                target_idx = search_idx
                break

        if target_idx < 0:
            return [-1, -1]
        else:
            # forward run
            end_pos = target_idx
            print('\nforward run')
            for idx in range(target_idx, len(nums)):
                print(f'idx: {idx}, val: {nums[idx]}')
                if nums[idx] == target:
                    end_pos = idx
                else:
                    break
            
            # backwards run
            start_pos = target_idx
            print('\nbackwards run')
            for idx in range(target_idx, -1, -1):
                print(f'idx: {idx}, val: {nums[idx]}')
                if nums[idx] == target:
                    start_pos = idx
                else:
                    break

            return [start_pos, end_pos]




'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
long_arr = [
    1,3,4,4,4,4,5,5,6,7,
    7,7,7,7,7,7,7,8,8,8,
    9,9,12,12,15,15,15,15,15,15,
    15,15,17,17,18,19,20,21,21,21,
    21,21,21,21,21,21,21,23,23,23,
    23,25,26,29,33,33,33,35,35,40,
    40,40,40,41,44,47,47,49,50,50,
    50,50,50,55,55,55,57,60,60,61
]

test_cases = [
    ([[5,7,7,8,8,10], 8], [3,4]),
    ([[5,7,7,8,8,10], 6], [-1,-1]),
    ([[5,7,7,8,8,10], 10], [5,5]),
    ([long_arr, 7], [9,16]),
    ([long_arr, 44], [64,64]),
    ([long_arr, 21], [37,46]),
    ([long_arr, 33], [54,56]),
    ([long_arr, 48], [-1,-1]),
    ([long_arr, 13], [-1,-1]),
    ([long_arr, 61], [79,79]),
    ([long_arr, 1], [0,0]),
    ([[2,2], 2], [0,1]),
]

solution = Solution().searchRange

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
