# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 

sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=False)                             
# ----------------------------------------------------------

def licenseKeyFormatting(S: str, K: int) -> int:
    concatenated = ''.join(S.split('-')).upper()
    flipped = concatenated[::-1]
    
    ss = set(S.split('-'))
    if len(ss) == 1 and list(ss)[0] == '':
        return ''

    license_key = ''
    for idx, char in enumerate(flipped):
        license_key += char
        if (idx+1) % K == 0:
            license_key += '-'

    if license_key[-1] == '-':
        license_key = license_key[:-1]
    
    return license_key[::-1]


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    (["5F3Z-2e-9-w", 4], "5F3Z-2E9W"),
    (["2-5g-3-J", 2], "2-5G-3J"),
    (['r', 1], 'R'),
    (['---', 3], '')
]

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: licenseKeyFormatting(input[0], input[1])
    ).run()
