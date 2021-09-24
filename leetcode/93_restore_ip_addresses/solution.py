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
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        if len(s) < 4: return []
        return self.recurse(start=0, sections=4)

    def recurse(self, start: int, sections: int) -> List[str]:
        # print(f'{" " * (4-sections)}start: {start}, sections: {sections}')
        answers = list()
        if sections <= 0: return answers
        if sections == 1:
            candidate = self.s[start:]
            if self.is_valid_ip_integer(candidate):
                answers.append(candidate)
                # print(f'        candidate: {candidate}')
        else:
            for i in range(3):
                cur_head = self.s[start:start+i+1]
                # print(f'--> cur_head: {cur_head}')
                if not self.is_valid_ip_integer(cur_head): continue
                recursive_answers = self.recurse(start=start+i+1, sections=sections-1)
                # print(f'      cur_head: {cur_head}, recursive_answers: {recursive_answers}')
                answers.extend([cur_head + "." + r for r in recursive_answers])
        return answers

    def is_valid_ip_integer(self, num: str) -> bool:
        if len(num) == 0: return False
        if len(num) > 1 and num[0] == "0": return False
        if int(num) > 255: return False
        return True


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["25525511135"], ["255.255.11.135","255.255.111.35"]),
        (["0000"], ["0.0.0.0"]),
        (["1111"], ["1.1.1.1"]),
        (["010010"], ["0.10.0.10","0.100.1.0"]),
        (["101023"], ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]),
        ([""], []),
    ]

    Tester.factory(test_cases, func=lambda input: sol.restoreIpAddresses(*input)).run(unordered_output=True)
