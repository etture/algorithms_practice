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
    def simplifyPath(self, path: str) -> str:
        elements = [x for x in path.split("/") if x != ""] 
        root_dir = "/"
        tree = list()
        for e in elements:
            if e == ".": continue
            elif e == "..":
                if len(tree) > 0: tree.pop(-1)
            else:
                tree.append(e)
        return root_dir + "/".join(tree)



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["/home/"], "/home"),
        (["/../"], "/"),
        (["/home//foo/"], "/home/foo"),
        (["/a/./b/../../c/"], "/c"),
    ]

    Tester.factory(test_cases, func=lambda input: sol.simplifyPath(*input)).run(unordered_output=False)
