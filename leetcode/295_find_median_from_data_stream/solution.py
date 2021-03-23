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

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap, self.max_heap = list(), list()

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
        else:
            if num >= self.min_heap[0]:
                if len(self.min_heap) > len(self.max_heap):
                    heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                if len(self.max_heap) == 0:
                    heapq.heappush(self.max_heap, -num)
                else:
                    if len(self.max_heap) > len(self.min_heap):
                        if num >= -self.max_heap[0]:
                            heapq.heappush(self.min_heap, num)
                        else:
                            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                            heapq.heappush(self.max_heap, -num)
                    else:
                        heapq.heappush(self.max_heap, -num)
        # print(f'input: {num}, min_heap: {self.min_heap}, max_heap: {self.max_heap}') 

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            # print(f'median: {round((self.min_heap[0] + -self.max_heap[0]) / 2, 1)}')
            return round((self.min_heap[0] + -self.max_heap[0]) / 2, 1)
        elif len(self.min_heap) > len(self.max_heap):
            # print(f'median: {round(self.min_heap[0] * 1.0, 1)}')
            return round(self.min_heap[0] * 1.0, 1)
        else:
            # print(f'median: {round(-self.max_heap[0] * 1.0, 1)}')
            return round(-self.max_heap[0] * 1.0, 1)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    def runner(commands: List[str], params: List[List[int]]) -> List[float]:
        ans = list()
        for idx, command in enumerate(commands):
            if command == "MedianFinder":
                mf = MedianFinder()
                ans.append(None)
            elif command == "addNum":
                mf.addNum(params[idx][0])
                ans.append(None)
            elif command == "findMedian":
                ans.append(mf.findMedian())
        return ans


    test_cases = [
        ([
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []]
        ], [None, None, None, 1.5, None, 2.0]),
        ([
            ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
            [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
        ], [None, None, -1.0, None, -1.5, None, -2.0, None, -2.5, None, -3.0]),
        (
            [
                ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
                [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
        ], [None,None,6.00000,None,8.00000,None,6.00000,None,6.00000,None,6.00000,None,5.50000,None,6.00000,None,5.50000,None,5.00000,None,4.00000,None,3.00000]),
        (
            [
                ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
                [[],[12],[],[10],[],[13],[],[11],[],[5],[],[15],[],[1],[],[11],[],[6],[],[17],[],[14],[],[8],[],[17],[],[6],[],[4],[],[16],[],[8],[],[10],[],[2],[],[12],[],[0],[]]
            ], [None,None,12.00000,None,11.00000,None,12.00000,None,11.50000,None,11.00000,None,11.50000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,11.00000,None,10.50000,None,10.00000,None,10.50000,None,10.00000]),
            (
                [
                    ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],
                    [[],[40],[],[12],[],[16],[],[14],[],[35],[],[19],[],[34],[],[35],[],[28],[],[35],[],[26],[],[6],[],[8],[],[2],[],[14],[],[25],[],[25],[],[4],[],[33],[],[18],[],[10],[],[14],[],[27],[],[3],[],[35],[],[13],[],[24],[],[27],[],[14],[],[5],[],[0],[],[38],[],[19],[],[25],[],[11],[],[14],[],[31],[],[30],[],[11],[],[31],[],[0],[]]
                ], [None,None,40.00000,None,26.00000,None,16.00000,None,15.00000,None,16.00000,None,17.50000,None,19.00000,None,26.50000,None,28.00000,None,31.00000,None,28.00000,None,27.00000,None,26.00000,None,22.50000,None,19.00000,None,22.00000,None,25.00000,None,22.00000,None,25.00000,None,22.00000,None,19.00000,None,18.50000,None,19.00000,None,18.50000,None,19.00000,None,18.50000,None,19.00000,None,21.50000,None,19.00000,None,18.50000,None,18.00000,None,18.50000,None,19.00000,None,19.00000,None,19.00000,None,18.50000,None,19.00000,None,19.00000,None,19.00000,None,19.00000,None,19.00000]),
    ]

    Tester.factory(test_cases, func=lambda input: runner(*input)).run(unordered_output=False)
