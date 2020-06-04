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
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        return []        

        

'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    ([["area","lead","wall","lady","ball"]], 
        [
            [ "wall",
                "area",
                "lead",
                "lady"
            ],
            [ "ball",
                "area",
                "lead",
                "lady"
            ]
        ]
    ),
    ([["abat","baba","atan","atal"]], 
        [
            [ "baba",
                "abat",
                "baba",
                "atan"
            ],
            [ "baba",
                "abat",
                "baba",
                "atal"
            ]
        ]
    )
]

solution = Solution().wordSquares

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run(unordered_output=True)
