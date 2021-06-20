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

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv_store = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_store:
            self.kv_store[key] = list()
        self.kv_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store: return ""
        # print(f'key: {key}, timestamp: {timestamp}, kv_store: {self.kv_store[key]}')
        values = self.kv_store[key]
        left, right = 0, len(values)-1
        last_middle = 0
        while left <= right:
            middle = (left + right) // 2
            if values[middle][0] == timestamp:
                last_middle = middle
                break
            elif values[middle][0] < timestamp:
                last_middle = middle
                left = middle + 1
            else:
                right = middle - 1
                
        # print(f'    last_middle: {last_middle}, values[last_middle]: {values[last_middle]}')
        if values[last_middle][0] <= timestamp:
            return values[last_middle][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

class Solution:
    def run(self, operations: List[str], parameters: List[str|int]):
        timemap = TimeMap()
        answer = list()
        for idx in range(len(operations)):
            op, params = operations[idx], parameters[idx]
            if op == "TimeMap":
                answer.append(None)
            elif op == "set":
                answer.append(timemap.set(*params))
            elif op == "get":
                answer.append(timemap.get(*params))
        return answer



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([
            ["TimeMap","set","get","get","set","get","get"],
            [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
        ], [None,None,"bar","bar",None,"bar2","bar2"]),
        ([
            ["TimeMap","set","set","get","get","get","get","get"],
            [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
        ], [None,None,None,"","high","high","low","low"]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.run(*input)).run(unordered_output=False)
