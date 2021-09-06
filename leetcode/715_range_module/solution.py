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

class RangeModule:

    def __init__(self):
        # self.ranges = list()
        self.ranges = [(10, 20), (22, 25), (30, 50)]
        print(self.find_biggest_smaller_idx(9))
        print(self.find_biggest_smaller_idx(11))
        print(self.find_biggest_smaller_idx(23))
        print(self.find_biggest_smaller_idx(35))

    def find_biggest_smaller_idx(self, val: int) -> int:
        if len(self.ranges) == 0: return -1
        if len(self.ranges) == 1:
            if val < self.ranges[0][0]:
                return -1
            else:
                return 0
        left, right = 0, len(self.ranges) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.ranges[mid][0] > val:
                if mid == 0:
                    return -1
                right = mid
            elif self.ranges[mid][0] <= val:
                # print(f'left: {left}, right: {right}, mid: {mid}')
                if mid == 0:
                    return mid
                elif mid + 1 >= len(self.ranges):  # there is no more to right
                    return mid
                elif mid + 1 < len(self.ranges) and self.ranges[mid+1][0] > val:
                    return mid
                else:
                    left = mid + 1



    def addRange(self, left: int, right: int) -> None:
        if len(self.ranges) == 0:
            self.ranges.append((left, right))
        else:
            left_biggest_smaller = self.find_biggest_smaller_idx(left)
            right_biggest_smaller = self.find_biggest_smaller_idx(right)
            if self.ranges[left_biggest_smaller][1] < left:  # left doesn't overlap
                start_insert_idx = left_biggest_smaller
            else:  # have to merge left
                



    def queryRange(self, left: int, right: int) -> bool:
        pass

    def removeRange(self, left: int, right: int) -> None:
        pass


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
            
class Solution:
    def run(self, commands: List[str], params: List[List[int]]) -> List[int]:
        ans = list()
        for i in range(len(commands)):
            command = commands[i]
            param = params[i]
            if command == "RangeModule":
                obj = RangeModule()
                ans.append(None)
            elif command == "addRange":
                ans.append(obj.addRange(*param))
            elif command == "queryRange":
                ans.append(obj.queryRange(*param))
            elif command == "removeRange":
                ans.append(obj.removeRange(*param))
        return ans


            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [
                ["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"],
                [[],[10,20],[14,16],[10,14],[13,15],[16,17]]
            ],
            [None, None, None, True, False, True]
        ),
    ]

    Tester.factory(test_cases, func=lambda input: sol.run(*input)).run(unordered_output=False)
