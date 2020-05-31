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

def solution(A: List[int]) -> int:
    def can_jump_idx(cur_idx, cur_num, subsequence, gte):
        print(f'subsequence: {subsequence}')
        if gte:
            min_possible = 9999999
            min_idx = -1
            for idx, n in enumerate(subsequence):
                if n >= cur_num:
                    if n < min_possible:
                        min_possible = n
                        min_idx = idx
            return min_idx + 1 + cur_idx if min_idx >= 0 else min_idx
        else:   
            max_possible = -1
            min_idx = -1
            for idx, n in enumerate(subsequence):
                print(f'idx: {idx}, n: {n}')
                if n <= cur_num:
                    print(f'n ({n}) <= cur_num ({cur_num})')
                    if n > max_possible:
                        print(f'n ({n}) > max_possible ({max_possible})')
                        max_possible = n
                        min_idx = idx
            print(f'min_idx: {min_idx}, cur_idx: {cur_idx}')
            return min_idx + 1 + cur_idx if min_idx >= 0 else min_idx

    can_reach_end = 0
    for start_idx in range(len(A)):
        print(' ')
        if start_idx == len(A)-1:
            can_reach_end += 1
            continue
        cur_idx = start_idx
        cur_num = A[start_idx]
        gte = True
        can_jump_to = -2
        while cur_idx not in (-1, len(A)-1):
            print(f'cur_idx: {cur_idx}, cur_num: {cur_num}, gte: {gte}, A[cur_idx:]: {A[cur_idx+1:]}')
            cur_idx = can_jump_idx(cur_idx, cur_num, A[cur_idx+1:], gte)
            print(f'result idx: {cur_idx}')
            cur_num = A[cur_idx]
            gte = not gte
        if cur_idx == len(A)-1:
            print('can reach end')
            can_reach_end += 1
    
    return can_reach_end
            


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    ([[2,3,1,1,4]], 3),
    ([[5,1,3,4,2]], 3),
    ([[10,13,12,14,15]], 2),
    ([[81,54,96,60,58]], 2)
]

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(input[0])
    ).run()
