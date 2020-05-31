'''
Give an array of boxes with size N+1 with its weight is from 1->N. The final element is empty marked with an 0. Sort the boxes from lightest to heaviest where you can only move 1 box at a time to the empty slot. You should do it in o(N) time.
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

def solution(boxes):
    N = len(boxes) - 1
    reverse_lookup = [0] * (N + 1)
    for idx, weight in enumerate(boxes):
        reverse_lookup[weight] = idx
    # print(reverse_lookup)
    for weight in range(1, N + 1):
        arr_pos = weight - 1
        # print(f'Weight: {weight}, arr_pos: {arr_pos}, boxes: {boxes}, reverse_lookup: {reverse_lookup}')
        if boxes[arr_pos] != weight:
            # Switch box in my place with zero
            box_in_my_place = boxes[arr_pos]
            target_pos, empty_pos = reverse_lookup[box_in_my_place], reverse_lookup[0]
            # Switch reverse lookup table
            tmp = reverse_lookup[box_in_my_place]
            reverse_lookup[box_in_my_place] = reverse_lookup[0]
            reverse_lookup[0] = tmp
            # Switch boxes array
            tmp = boxes[target_pos]
            boxes[target_pos] = boxes[empty_pos]
            boxes[empty_pos] = tmp
            # print(f'    Switched box in my place, boxes: {boxes}, reverse_lookup: {reverse_lookup}')
            
            # Then switch target with zero
            target_pos, empty_pos = reverse_lookup[weight], reverse_lookup[0]
            # Switch reverse lookup table
            tmp = reverse_lookup[weight]
            reverse_lookup[weight] = reverse_lookup[0]
            reverse_lookup[0] = tmp
            # Switch boxes array
            tmp = boxes[target_pos]
            boxes[target_pos] = boxes[empty_pos]
            boxes[empty_pos] = tmp
            # print(f'    Switched target weight, boxes: {boxes}, reverse_lookup: {reverse_lookup}')

        # print(f'    Final boxes: {boxes}, reverse_lookup: {reverse_lookup}\n')
    return boxes

# boxes==[3, 2, 4, 1, 5, 0] rl = [5, 3, 1, 0, 2, 4]
# Moving "one"
# rl move inter => boxes[1-1==0] == 3, so rl[3] == 0 && rl[0] == 5
#   SO DO:
#       box_in_my_place = boxes[target-1==1-1==0]==3
#       target_pos, empty_pos = rl[box_in_my_place==3], rl[0]
#       rl[box_in_my_place] <-> rl[0]
#       boxes[target_pos] <-> boxes[empty_pos]
#       
#   so tmp = rl[3] (0)
#   rl[3] = rl[0]
#   rl[0] = tmp
#   tmp = boxes[rl[3]==0]
#   boxes[rl[3]==0] = boxes[rl[0]==5]
#   boxes[rl[0]==5] = tmp
#   SO: boxes==[0, 2, 4, 1, 5, 3] rl = [0, 3, 1, 5, 2, 4]
#   THEN:
#       target_pos, empty_pos = rl[target==1], rl[0]
#       rl[target==1] <-> rl[0]
#       boxes[target_pos] <-> boxes[empty_pos]




'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
import random

def shuffled_input(N):
    arr = [0] * N
    for num in range(1, N+1):
        arr[num-1] = num
    random.shuffle(arr)
    arr.extend([0])
    return arr

def sorted_answer(N):
    arr = [0] * N
    for num in range(1, N+1):
        arr[num-1] = num
    arr.extend([0])
    return arr

test_cases = [
    ([[3, 2, 4, 1, 5, 0]], [1, 2, 3, 4, 5, 0]),
    ([[6, 1, 4, 5, 3, 2, 0]], [1, 2, 3, 4, 5, 6, 0]),
    ([shuffled_input(400)], sorted_answer(400)),
    ([shuffled_input(400000)], sorted_answer(400000)),
    ([shuffled_input(2000000)], sorted_answer(2000000)),
]

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(input[0])
    ).run()

    # import random
    # size = 200000
    # arr = [0] * size
    # for num in range(1, size+1):
    #     arr[num-1] = num
    # # random.shuffle(arr)
    # arr.extend([0])
    # print(arr)