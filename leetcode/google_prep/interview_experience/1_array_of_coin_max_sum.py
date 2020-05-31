'''
https://leetcode.com/discuss/interview-experience/645962/Google-or-SWE-2020-or-Rejected
<Sliding window problem>

Get maximum sum from array of coin, if you can only pick k coins from either side of the the array.

https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''

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
logger = Logger(verbose=False)                             
# ----------------------------------------------------------

class Solution:
    def maxScore_timeout(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        elif k == 1:
            if cardPoints[0] > cardPoints[-1]:
                return cardPoints[0]
            else:
                return cardPoints[-1]
        else:
            max_sum = 0
            for left in range(k, -1, -1):
                right = k - left
                left_arr = cardPoints[:left]
                right_arr = [] if right == 0 else cardPoints[-right:]
                iter_sum = sum(left_arr) + sum(right_arr)
                if iter_sum > max_sum:
                    max_sum = iter_sum
            return max_sum

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        elif k == 1:
            if cardPoints[0] > cardPoints[-1]:
                return cardPoints[0]
            else:
                return cardPoints[-1]
        else:
            cur_sum = sum(cardPoints[:k])
            max_sum = cur_sum
            cur_left_end_idx = k - 1 # until this becomes -1
            cur_right_start_idx = -1 # progress -= 1
            while cur_left_end_idx >= 0:
                cur_sum -= cardPoints[cur_left_end_idx]
                cur_sum += cardPoints[cur_right_start_idx]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                cur_left_end_idx -= 1
                cur_right_start_idx -= 1
            return max_sum


# LESSON: for python, use array access instead of list splicing
# List splicing for every loop takes a long time


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    ([[1,2,3,4,5,6,1], 3], 12),
    ([[2,2,2], 2], 4),
    ([[9,7,7,9,7,7,9], 7], 55),
    ([[1,1000,1], 1], 1),
    ([[1,79,80,1,1,1,200,1], 3], 202),
]


if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: Solution().maxScore(input[0], input[1])
    ).run()