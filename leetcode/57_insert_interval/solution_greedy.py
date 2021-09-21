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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = list()
        new_added = False
        for idx, elem in enumerate(intervals):
            # print(f'answer: {answer}')
            if elem[0] < newInterval[0]:
                answer.append(elem)
                continue
            if not new_added:
                if len(answer) == 0:
                    answer.append(newInterval)
                elif answer[-1][0] <= newInterval[0] <= answer[-1][1]:
                    # print(f'max: {max(answer[-1][1], newInterval[1])}')
                    answer[-1][1] = max(answer[-1][1], newInterval[1])
                else:
                    answer.append(newInterval)
                new_added = True
            if answer[-1][0] <= elem[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], elem[1])
            else:
                answer.append(elem)

        if not new_added:
            if len(answer) == 0:
                answer.append(newInterval)
            elif answer[-1][0] <= newInterval[0] <= answer[-1][1]:
                # print(f'max: {max(answer[-1][1], newInterval[1])}')
                answer[-1][1] = max(answer[-1][1], newInterval[1])
            else:
                answer.append(newInterval)

        return answer



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1,3],[6,9]], [2,5]], [[1,5],[6,9]]),
        ([[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]], [[1,2],[3,10],[12,16]]),
        ([[[1,2],[3,5],[6,7],[9,10],[12,16]], [4,8]], [[1,2],[3,8],[9,10],[12,16]]),
        ([[], [5,7]], [[5,7]]),
        ([[[1,5]], [2,3]], [[1,5]]),
        ([[[1,5]], [2,7]], [[1,7]]),
        ([[[1,3],[4,9],[11,20]], [0,100]], [[0,100]]),
        ([[[10,100],[101,200]], [1,2]], [[1,2],[10,100],[101,200]]),
        ([[[1,5]], [0,3]], [[0,5]]),
        ([[[0,5],[9,12]], [7,16]], [[0,5],[7,16]]),
        ([[[0,3],[6,8],[9,12]], [0,4]], [[0,4],[6,8],[9,12]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.insert(*input)).run(unordered_output=False)
