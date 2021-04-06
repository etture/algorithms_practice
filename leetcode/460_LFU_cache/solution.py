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

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.filled = 0
        self.timestamp = 0
        self.cache = dict()  # key: cache key, val: value
        self.counters = dict()  # key: cache key, val: counter
        self.frequency = dict()  # key: counter, val: list of cache keys
        self.times = dict()  # key: cache key, val: timestamp

    def get(self, key: int) -> int:
        if key in self.cache:
            self.times[key] = self.timestamp
            self.timestamp += 1
            self.counters[key] += 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print(f'put -> key: {key}, val: {value}, cache: {self.cache}, filled: {self.filled}')
        if self.capacity <= 0: 
            return
        if not self.is_full() and key not in self.cache:
            self.cache[key] = value
            self.counters[key] = 1
            self.times[key] = self.timestamp
            self.timestamp += 1
            self.filled += 1
        elif key in self.cache:
            self.cache[key] = value
            self.counters[key] += 1
            self.times[key] = self.timestamp
            self.timestamp += 1
        else:
            counter_values = sorted(self.counters.items(), key=lambda x: x[1])
            minimum = counter_values[0][1]
            # print(f'min counter: {minimum}')
            keys_with_min_counter = list()
            for k, counter in counter_values:
                if counter > minimum:
                    break
                keys_with_min_counter.append(k)
            # print(f'keys_with_min_counter: {keys_with_min_counter}')
            min_timestamp = 99999999
            min_timestamp_key = -1
            for k in keys_with_min_counter:
                if self.times[k] < min_timestamp:
                    min_timestamp = self.times[k]
                    min_timestamp_key = k
            # print(f'min_timestamp_key: {min_timestamp_key}')
            del self.cache[min_timestamp_key]
            del self.counters[min_timestamp_key]
            del self.times[min_timestamp_key]
            self.cache[key] = value
            self.counters[key] = 1
            self.times[key] = self.timestamp
            self.timestamp += 1
        # print(f'cache: {self.cache}')


    def is_full(self) -> bool:
        return self.filled >= self.capacity


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            
class Solution:
    def run(self, commands: List[str], params: List[List[int]]) -> List[int]:
        ans = list()
        for i in range(len(commands)):
            command = commands[i]
            param = params[i]
            if command == "LFUCache":
                obj = LFUCache(*param)
                ans.append(None)
            elif command == "get":
                ans.append(obj.get(*param))
            elif command == "put":
                ans.append(obj.put(*param))
        return ans


            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [
                ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
            ],
            [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
        ),
        (
            [
                ["LFUCache","put","get"],
                [[0],[0,0],[0]]
            ],
            [None, None, -1]
        ),
        (
            [
                ["LFUCache","put","put","get","put","put","get"],
                [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
            ],
            [None,None,None,2,None,None,2]
        ),
    ]

    Tester.factory(test_cases, func=lambda input: sol.run(*input)).run(unordered_output=False)
