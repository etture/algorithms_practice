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

def numUniqueEmails(emails: List[str]) -> int:
    email_set = set()
    for email in emails:
        print('')
        local_name, domain_name = email.split('@')
        print(f'domain: {domain_name}')
        pre_plus = local_name.split('+')[0]
        print(f'preplus: {pre_plus}')
        local_name = ''.join(pre_plus.split('.'))
        print(f'local: {local_name}')
        email_set.add('@'.join([local_name, domain_name]))
        print('@'.join([local_name, domain_name]))
    return len(email_set)


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    ([[
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
        ]], 2),
    ([["test.email+alex@leetcode.com", "test.email@leetcode.com"]], 1)
]

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: numUniqueEmails(input[0])
    ).run()
