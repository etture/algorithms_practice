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

import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start_combo = "0000"
        if target == start_combo: return 0
        if start_combo in deadends: return -1

        def spin_one(combo: str) -> Iterator[str]:
            for i in range(4):
                x = int(combo[i])
                for d in [1, -1]:
                    spun_digit = (x + d) % 10
                    yield combo[:i] + str(spun_digit) + combo[i+1:]

        queue = collections.deque([(start_combo, 1)])
        seen = set([start_combo])
        while len(queue) > 0:
            combo, depth = queue.popleft()
            if combo in deadends: continue
            for spun in spin_one(combo):
                if spun in seen or spun in deadends: continue
                if spun == target: return depth
                seen.add(spun)
                queue.append((spun, depth + 1))
        return -1


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([["0201","0101","0102","1212","2002"], "0202"], 6),
        ([["8888"], "0009"], 1),
        ([["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"], -1),
        ([["0000"], "8888"], -1),
        ([["1234"], "0000"], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.openLock(*input)).run(unordered_output=False)
