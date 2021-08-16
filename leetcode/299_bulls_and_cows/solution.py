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
    def getHint(self, secret: str, guess: str) -> str:
        # orig_map = dict()
        # for idx, orig_digit in enumerate([int(a) for a in list(secret)]):
        #     if orig_digit not in orig_map:
        #         orig_map[orig_digit] = list()
        #     orig_map[orig_digit].append(idx)
        # print(orig_map)

        # bulls, cows = 0, 0
        # for idx, new_digit in enumerate([int(a) for a in list(guess)]):
        #     if new_digit in orig_map:
        #         if idx in orig_map[new_digit]:
        #             bulls += 1
        #             orig_map[new_digit].remove(idx)
        #         else:
        #             cows += 1
        #             orig_map[new_digit].pop()
        #         if len(orig_map[new_digit]) <= 0:
        #             del orig_map[new_digit]
        
        # return f'{bulls}A{cows}B'

        bulls, cows = 0, 0
        secret_cnt, guess_cnt = [0] * 10, [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_cnt[int(secret[i])] += 1
                guess_cnt[int(guess[i])] += 1
        print(bulls)

        for i in range(10):
            if guess_cnt[i] > 0 and secret_cnt[i] > 0:
                cows += min(guess_cnt[i], secret_cnt[i])
        print(cows)

        print(f's: {secret_cnt}')
        print(f'g: {guess_cnt}')
            
        return f'{bulls}A{cows}B'

if __name__ == '__main__':

    sol = Solution()

    test_cases = [
        (["1807", "7810"], "1A3B"),
        (["1807", "7800"], "2A1B"),
        (["1123", "0111"], "1A1B"),
        (["1100", "0110"], "2A2B"),
        (["1100", "0000"], "2A0B"),
        (["1", "0"], "0A0B"),
        (["1", "1"], "1A0B"),
    ]
    Tester.factory(test_cases, func=lambda input: sol.getHint(*input)).run(unordered_output=False)
