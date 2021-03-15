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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]: # graph DFS based
        email_to_name = dict()
        graph = defaultdict(set) # key: head node, value: set of connected tail nodes
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                email_to_name[email] = name

        seen = set()
        ans = list()
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                combined = list()
                while stack:
                    elem = stack.pop()
                    combined.append(elem)
                    for nei in graph[elem]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([email_to_name[email], *sorted(combined)])
        return ans


    def accountsMerge_class_based(self, accounts: List[List[str]]) -> List[List[str]]:
        class Account:
            def __init__(self, name: str, emails: List[str] = None):
                self.name = name
                self.emails = set() if emails is None else set(emails)

            def add_email(self, email: str):
                self.emails.add(email)

            def merge_emails(self, emails: List[str]|Set[str]):
                self.emails.update(emails)

            def get_output(self) -> List[str]:
                return [self.name, *sorted(self.emails)]

            def __repr__(self) -> str:
                return f'<Account name={self.name}, emails={self.emails}>'

        email_to_account_map = dict()
        accounts_list = set()
        for idx, account in enumerate(accounts):
            has_counterpart = False
            name = account[0]
            merge_account = Account(name)
            seen_emails = set()
            
            for email in account[1:]:
                merge_account.add_email(email)
                
                # print(f'  email: {email}, seen_emails: {seen_emails}, email_to_account_map[email]: {email_to_account_map[email] if email in email_to_account_map else None}')
                if email in email_to_account_map and email not in seen_emails:
                    # print(f'    email: {email}, entered if')
                    has_counterpart = True
                    old_account = email_to_account_map[email]
                    merge_account.merge_emails(old_account.emails)
                    seen_emails.update(old_account.emails)
                    if old_account in accounts_list:
                        accounts_list.remove(old_account)
                else:
                    seen_emails.add(email)

            if has_counterpart:
                # print(f'**has_counterpart, seen_emails: {seen_emails}')
                for seen_email in seen_emails:
                    email_to_account_map[seen_email] = merge_account
                    accounts_list.add(merge_account)
            else:
                new_account = Account(name, account[1:])
                accounts_list.add(new_account)
                for email in account[1:]:
                    email_to_account_map[email] = new_account

            # print(f'Iteration {idx+1}, accounts_list: {accounts_list}')

        # print(accounts_list)
        return [a.get_output() for a in accounts_list]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]], [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]),
        ([[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]], [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]),
        ([[["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]], 
        [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.accountsMerge(*input)).run(unordered_output=True)
