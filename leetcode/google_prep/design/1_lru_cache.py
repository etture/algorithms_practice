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


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_stack = list()
        self.cache_dict = dict()

    def is_full(self) -> bool:
        return len(self.key_stack) == self.capacity

    def push_key_to_end(self, key: int) -> None:
        for idx in range(len(self.key_stack)):
            if self.key_stack[idx] == key:
                self.key_stack.pop(idx)
                self.key_stack.append(key)
                break

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        self.push_key_to_end(key)
        return self.cache_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.cache_dict[key] = value
            self.push_key_to_end(key)
        else:
            if self.is_full():
                old_key = self.key_stack.pop(0)
                del self.cache_dict[old_key]
            self.key_stack.append(key)
            self.cache_dict[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output


if __name__ == '__main__':
    cache = LRUCache(2) # capacity

    # cache.put(1, 1)
    # cache.put(2, 2)
    # assert cache.get(1) == 1       # returns 1
    # cache.put(3, 3)    # evicts key 2
    # assert cache.get(2) == -1       # returns -1 (not found)
    # cache.put(4, 4)    # evicts key 1
    # assert cache.get(1) == -1       # returns -1 (not found)
    # assert cache.get(3) == 3       # returns 3
    # assert cache.get(4) == 4       # returns 4

    cache.put(2,1)
    print(cache.key_stack)
    cache.put(2,2)
    print(cache.key_stack)
    assert cache.get(2) == 2
    print(cache.key_stack)
    cache.put(1,1)
    print(cache.key_stack)
    cache.put(4,1)
    print(cache.key_stack)
    assert cache.get(2) == -1
    print(cache.key_stack)
