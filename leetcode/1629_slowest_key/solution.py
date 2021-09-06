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
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        durations = list()
        for i in range(len(releaseTimes)):
            if i == 0:
                durations.append(releaseTimes[i])
            else:
                durations.append(releaseTimes[i] - releaseTimes[i-1])
        # print(durations)
        max_dur = 0
        keys_set = set()
        for idx, dur in enumerate(durations):
            if dur == max_dur:
                keys_set.add(keysPressed[idx])
            elif dur > max_dur:
                max_dur = dur
                keys_set = set([keysPressed[idx]])
        # print(keys_set)
        return max(keys_set)
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[9,29,49,50], "cbcd"], "c"),
        ([[12,23,36,46,62], "spuda"], "a"),
    ]

    Tester.factory(test_cases, func=lambda input: sol.slowestKey(*input)).run(unordered_output=False)
