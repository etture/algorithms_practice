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

def solution(px):
    min_prior = 99999999
    max_diff = -1
    for idx, price in enumerate(px):
        if price > min_prior and idx > 0:
            if price - min_prior > max_diff:
                max_diff = price - min_prior
        else:
            min_prior = price
    return max_diff


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    ([[7, 5, 3, 1]], -1),
    ([[7, 1, 2, 5]], 4),
    ([[-129, 877, -166, 433, 547, 413, 311, 311, 307, 15, 334, -58, 821, 335, 646, 697, 845, -156, 781, -84, 675, 833, 182, 937, -246, 865, 603, 534, 912, 618, 494, -73, 131, 28, 282, 412, 489, 902, 842, 259, 844, 720, 324, -154, 757, 662, 628, -5, 163, 178, -7, -18, 365, 303, 530, 744, 838, 626, -175, 216, 22, 976, 704, 782, 579, 151, 764, 494, -28, 699, 718, 351, 959, 407, 256, 215, 952, 328, 631, 228, 711, 438, 753, 830, 28, 81, 410, 621, 543, 745, 714, 829, 457, 481, 136, 134, 50, 678, -235, 256]], 1222),
]

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(input[0])
    ).run()
