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
logger = Logger(verbose=True)                             
# ----------------------------------------------------------


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def brute_force():
            max_area = 0
            for start_pos in range(len(height) - 1):
                for end_pos in range(1, len(height)):
                    width = end_pos - start_pos
                    hheight = min(height[start_pos], height[end_pos])
                    area = width * hheight
                    if area > max_area:
                        max_area = area
            return max_area

        def optimal():
            start_pos, end_pos = 0, len(height) - 1
            # w, h = (end_pos - start_pos), min(height[end_pos], height[start_pos])
            max_area = 0
            while start_pos < end_pos:
                w, h = (end_pos - start_pos), min(height[end_pos], height[start_pos])
                cur_area = w * h
                # print(f'start: {start_pos}, end: {end_pos}, cur_area: {cur_area}, max_area: {max_area}')
                if cur_area > max_area:
                    max_area = cur_area
                if height[start_pos] < height[end_pos]:
                    # print('left is smaller')
                    pos = start_pos + 1
                    while pos < end_pos:
                        if height[pos] > height[start_pos]:
                            start_pos = pos
                            break
                        pos += 1
                    if pos == end_pos:
                        break
                else:
                    # print('right is smaller')
                    pos = end_pos - 1
                    while pos > start_pos:
                        if height[pos] > height[end_pos]:
                            end_pos = pos
                            break
                        pos -= 1
                    if pos == start_pos:
                        break
            return max_area

        return optimal()

        

'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    ([[1,8,6,2,5,4,8,3,7]], 49),
    # ([[1,8,6,15,5,4,8,20,7]], 60),
    # ([[6,4,3,1,4,6,99,62,1,2,6]], 62),  
    # ([[76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]], 18048),
    # ([[1000,1000,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]], 1000),
]

solution = Solution().maxArea

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
