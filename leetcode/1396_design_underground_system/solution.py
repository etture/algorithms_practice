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


class UndergroundSystem:

    def __init__(self):
        self.customer_log = dict()
        self.average_times = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_log[id] = tuple([stationName, t])
        if stationName not in self.average_times:
            self.average_times[stationName] = dict()

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        enter_stationName, enter_time = self.customer_log[id]
        del self.customer_log[id]
        time_taken = t - enter_time
        if stationName not in self.average_times[enter_stationName]:
            self.average_times[enter_stationName][stationName] = list()
        self.average_times[enter_stationName][stationName].append(time_taken)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times_list = self.average_times[startStation][endStation]
        return round(sum(times_list) / len(times_list), 5)


class Solution:
    def run(self, commands: List[str], params: List[List]) -> List[float]:
        obj = UndergroundSystem()
        answer = list()
        for idx in range(len(commands)):
            command = commands[idx]
            # print(f'command: {command}, params: {params[idx]}')
            if command == "UndergroundSystem":
                answer.append(None)
            elif command == "checkIn":
                answer.append(obj.checkIn(*params[idx]))
            elif command == "checkOut":
                answer.append(obj.checkOut(*params[idx]))
            elif command == "getAverageTime":
                answer.append(obj.getAverageTime(*params[idx]))
        return answer


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([
            ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"],
            [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
        ], 
        [None,None,None,None,None,None,None,14.00000,11.00000,None,11.00000,None,12.00000]),
        ([
            ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"],
            [[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
        ],
        [None,None,None,5.00000,None,None,5.50000,None,None,6.66667]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.run(*input)).run(unordered_output=False)
