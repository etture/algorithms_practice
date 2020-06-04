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
    def findStrobogrammatic(self, n: int) -> List[str]:
        strobo_pairs = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        outers = ['0', '1', '6', '8', '9']

        def build(length: int):
            if length == 1:
                return ['0', '1', '8']
            elif length == 2:
                return ['00', '11', '69', '88', '96']
            else:
                inners = build(length - 2)
                cur_set = list()
                for outer in outers:
                    for inner in inners:
                        cur_set.append(f'{outer}{inner}{strobo_pairs[outer]}')
                return cur_set

        return [elem for elem in build(n) if elem[0] != '0' or len(elem) == 1]



'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    ([1], ["0","1","8"]),
    ([2], ["11","69","88","96"]),
    ([3], ["101","111","181","609","619","689","808","818","888","906","916","986"]),
    ([4], ["1001","1111","1691","1881","1961","6009","6119","6699","6889","6969","8008","8118","8698","8888","8968","9006","9116","9696","9886","9966"]),
    ([6], ["100001","101101","106901","108801","109601","110011","111111","116911","118811","119611","160091","161191","166991","168891","169691","180081","181181","186981","188881","189681","190061","191161","196961","198861","199661","600009","601109","606909","608809","609609","610019","611119","616919","618819","619619","660099","661199","666999","668899","669699","680089","681189","686989","688889","689689","690069","691169","696969","698869","699669","800008","801108","806908","808808","809608","810018","811118","816918","818818","819618","860098","861198","866998","868898","869698","880088","881188","886988","888888","889688","890068","891168","896968","898868","899668","900006","901106","906906","908806","909606","910016","911116","916916","918816","919616","960096","961196","966996","968896","969696","980086","981186","986986","988886","989686","990066","991166","996966","998866","999666"])
]

solution = Solution().findStrobogrammatic

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
