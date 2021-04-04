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

from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        owes_map = defaultdict(set)
        balance_map = defaultdict(lambda: 0)
        for t in transactions:
            sender, receiver, amount = t
            owes_map[receiver].add(sender)
            balance_map[sender] -= amount
            balance_map[receiver] += amount

        print(f'owes_map: {owes_map}')
        print(f'balance_map: {balance_map}')

        debtor_map = defaultdict(lambda: 0)
        creditor_map = defaultdict(lambda: 0)
        for person, balance in balance_map.items():
            if balance == 0:
                continue
            elif balance > 0:
                debtor_map[person] = balance
            else:
                creditor_map[person] = balance

        debtors = sorted([[person, amount] for person, amount in debtor_map.items()], key=lambda x: x[1], reverse=True)
        creditors = sorted([[person, amount] for person, amount in creditor_map.items()], key=lambda x: x[1])
        transction_cnt = 0

        print(f'debtors: {debtors}')
        print(f'creditors: {creditors}')

        d_idx, c_idx = 0, 0
        d_idx_to_pop, c_idx_to_pop = list(), list()
        while d_idx < len(debtors) and c_idx < len(creditors):
            if debtors[d_idx][1] == -creditors[c_idx][1]:
                d_idx_to_pop.append(d_idx)
                c_idx_to_pop.append(c_idx)
                d_idx += 1
                c_idx += 1
                transction_cnt += 1
            elif debtors[d_idx][1] < -creditors[c_idx][1]:
                c_idx += 1
            else:
                d_idx += 1

        print(f'd_idx_to_pop: {d_idx_to_pop}')
        print(f'c_idx_to_pop: {c_idx_to_pop}')

        debtors = [val for idx, val in enumerate(debtors) if idx not in d_idx_to_pop]
        creditors = sorted([val for idx, val in enumerate(creditors) if idx not in c_idx_to_pop], key=lambda x: -x[1])

        print(f'debtors: {debtors}')
        print(f'creditors: {creditors}')

        while len(debtors) > 0 and len(creditors) > 0:
            while_loop_run = False
            creditor_idx = 0
            for idx, c in enumerate(creditors):
                if debtors[0][1] == -c[1]:
                    creditor_idx = idx
                    break
                elif debtors[0][1] > -c[1]:
                    break
            while debtors[0][1] > 0 and creditors[creditor_idx][1] < 0:
                while_loop_run = True
                debtors[0][1] -= 1
                creditors[creditor_idx][1] += 1
            if while_loop_run: transction_cnt += 1

            print(f'  while loop run')
            print(f'    debtors: {debtors}')
            print(f'    creditors: {creditors}')
            
            if debtors[0][1] <= 0:
                debtors.pop(0)
            if creditors[creditor_idx][1] >= 0:
                creditors.pop(creditor_idx)

            debtors.sort(key=lambda x: x[1], reverse=True)
            creditors.sort(key=lambda x: x[1])
            print(f'     after sort run:')
            print(f'       debtors: {debtors}')
            print(f'       creditors: {creditors}')

        return transction_cnt



            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[0,1,10], [2,0,5]]], 2),
        ([[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]], 1),
        ([[[0,2,10],[0,3,6],[0,4,12]]], 3),
        ([[[0,2,10],[0,3,6],[0,4,12],[4,2,12],[3,2,6]]], 1),
        ([[[1,5,8],[8,9,8],[2,3,9],[4,3,1]]], 4),
        ([[[10,11,6],[12,13,7],[14,15,2],[14,16,2],[14,17,2],[14,18,2]]], 6),
        ([[[0,2,4],[1,2,4],[3,4,5]]], 3),
        ([[[1,2,3],[1,3,3],[6,4,1],[5,4,4]]], 4),
    ]

    Tester.factory(test_cases, func=lambda input: sol.minTransfers(*input)).run(unordered_output=False)
