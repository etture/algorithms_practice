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
import pprint
pp = pprint.PrettyPrinter()

class Solution:

    # at least 6 characters and at most 20 characters
    # at least one lowercase letter, uppercase letter, and digit
    # no 3 repeating characters in a row

    def strongPasswordChecker(self, password: str) -> int:
        cnt = 0
        pwd_length = len(password)
        need_lower, need_upper, need_digit = True, True, True
        cur_char = ''
        repeat_cnt = 1
        needs_replacing_due_to_repeat_cnt = 0

        modulo_list = list()

        for char in password:
            
            # check if password has at least one lowercase letter, uppercase letter, and digit
            if char in 'abcdefghijklmnopqrstuvwxyz':
                need_lower = False
            elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                need_upper = False
            elif char in '0123456789':
                need_digit = False

            # check repeating characters. number to replace = n // 3
            if char == cur_char:
                repeat_cnt += 1
            else:
                # print(f'char: {char}, cur_char: {cur_char}, repeat_cnt: {repeat_cnt}')
                needs_replacing_due_to_repeat_cnt += repeat_cnt // 3
                if repeat_cnt >= 3:
                    modulo_list.append(repeat_cnt % 3)
                cur_char = char
                repeat_cnt = 1
        needs_replacing_due_to_repeat_cnt += repeat_cnt // 3
        if repeat_cnt >= 3:
            modulo_list.append(repeat_cnt % 3)

        print(f'modulo_list: {modulo_list}')
        print(f'lower: {need_lower}, upper: {need_upper}, digit: {need_digit}, needs_replacing: {needs_replacing_due_to_repeat_cnt}')
        at_least_cnt = sum([need_lower, need_upper, need_digit])

        at_least_cnt -= needs_replacing_due_to_repeat_cnt

        modulo_cnt = 0
        if len(modulo_list) > 0:
            for _ in range(pwd_length - 20):
                min_val = 9999999999
                min_idx = -1
                for idx, m in enumerate(modulo_list):
                    if m < min_val:
                        min_val = m
                        min_idx = idx
                modulo_list[min_idx] -= 1
                if modulo_list[min_idx] < 0:
                    modulo_cnt += 1
                    modulo_list[min_idx] = 2

            print(f'modulo_cnt: {modulo_cnt}')

        if needs_replacing_due_to_repeat_cnt > 0:
            if pwd_length > 20:
                # needs_replacing_due_to_repeat_cnt -= pwd_length - 20
                needs_replacing_due_to_repeat_cnt -= modulo_cnt
            elif pwd_length < 6:
                needs_replacing_due_to_repeat_cnt -= 6 - pwd_length
                if needs_replacing_due_to_repeat_cnt < 0:
                    needs_replacing_due_to_repeat_cnt = 0

        cnt += needs_replacing_due_to_repeat_cnt

        print(f'needs_replacing: {needs_replacing_due_to_repeat_cnt}, at_least_cnt: {at_least_cnt}, tmp_cnt: {cnt}')

        
        if at_least_cnt > 0:
            cnt += at_least_cnt
            if pwd_length < 6:
                pwd_length += at_least_cnt

        if pwd_length < 6:
            cnt += 6 - pwd_length
        elif pwd_length > 20:
            cnt += pwd_length - 20

        print(f'pwd_length: {pwd_length}, at_least_cnt: {at_least_cnt}, cnt: {cnt}')
        return cnt
        



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["a"], 5),
        (["aA1"], 3),
        (["1337C0d3"], 0),
        (["13337C0d3"], 1),
        (["aaa"], 3),
        (["1234567891234567891234567890"], 10),
        (["abccccc1222222poii444"], 4),
        (["abccdcc12232q2poii4w4"], 2),
        (["aaaB1"], 1),
        (["bbaaaaaaaaaaaaaaacccccc"], 8),
        (["aaaabbbbccccddeeddeeddeedd"], 8),
    ]
# 23, 15, 6 
# "bbaaaaaaaaaaaaaccccc"
# 20, 13, 5
    Tester.factory(test_cases, func=lambda input: sol.strongPasswordChecker(*input)).run(unordered_output=False)
