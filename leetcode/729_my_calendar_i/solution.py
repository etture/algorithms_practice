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

class MyCalendar:

    def __init__(self):
        self.calendar = list()

    def book(self, start: int, end: int) -> bool:
        end = end - 1
        if len(self.calendar) == 0:
            self.calendar.append((start, end))
            return True

        # print(f'cal: {self.calendar} // start: {start}, end: {end}')
        
        start_idx, end_idx = 0, len(self.calendar)-1
        while start_idx <= end_idx:
            middle = (start_idx + end_idx) // 2
            date = self.calendar[middle]
            if date[0] <= start <= date[1] or date[0] <= end <= date[1]:
                return False
            if start > date[1]:
                if middle+1 >= len(self.calendar):  # no more to right, can book to right
                    self.calendar.append((start, end))
                    return True
                elif end < self.calendar[middle+1][0]:  # can book immediately to right
                    self.calendar = self.calendar[:middle+1] + [(start, end)] + self.calendar[middle+1:]
                    return True
                else:  # go right
                    start_idx = middle + 1
            elif end < date[0]:
                if middle-1 < 0:  # no more to left, can book to left
                    self.calendar = [(start, end)] + self.calendar
                    return True
                elif start > self.calendar[middle-1][1]:  # can book immediately to left
                    self.calendar = self.calendar[:middle] + [(start, end)] + self.calendar[middle:]
                    return True
                else:  # go left
                    end_idx = middle - 1
            else:
                return False
            
class Solution:
    def run(self, commands: List[str], params: List[int]) -> List[bool]:
        obj = MyCalendar()
        ans = list()
        for i in range(len(commands)):
            command = commands[i]
            param = params[i]
            if command == "MyCalendar":
                ans.append(None)
            elif command == "book":
                ans.append(obj.book(*param))
        return ans



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [
                ["MyCalendar","book","book","book"],
                [[],[10,20],[15,25],[20,30]]
            ],
            [None,True,False,True]
        ),
        (
            [
                ["MyCalendar","book","book","book","book","book","book","book","book","book","book"],
                [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
            ],
            [None,True,True,False,False,True,False,True,True,True,False]
        ),
    ]

    Tester.factory(test_cases, func=lambda input: sol.run(*input)).run(unordered_output=False)
