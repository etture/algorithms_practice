import sys
sys.path.append('/Users/jinoo/Documents/Dev/algo_practice')
import math
from collections import Counter

from utils.Tester import Tester, Logger

logger = Logger(verbose=True)

def check_alphabet(string):
    for char in string:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            continue
        else:
            return False
    return True

def get_alphabet_pairs(string):
    multiset = []
    for idx in range(len(string)-1):
        substring = string[idx:idx+2]
        if check_alphabet(substring):
            multiset.append(substring.upper())
    return multiset

def multiset_minmax(counter1, counter2, keys, minmax):
    cnt = 0
    for key in keys:
        cnt += minmax(counter1[key], counter2[key])
    return cnt

def multiset_intersection(counter1, counter2):
    set1 = set(counter1.keys())
    set2 = set(counter2.keys())
    intersection = set1.intersection(set2)
    return multiset_minmax(counter1, counter2, intersection, min)

def multiset_union(counter1, counter2):
    set1 = set(counter1.keys())
    set2 = set(counter2.keys())
    union = set1.union(set2)
    return multiset_minmax(counter1, counter2, union, max)

def jaccard_similarity(set1, set2):
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    intersection_cnt = multiset_intersection(counter1, counter2)
    union_cnt = multiset_union(counter1, counter2)
    if union_cnt == 0:
        return 1
    return float(intersection_cnt) / union_cnt

def solution(str1, str2):
    return math.floor(65536 * jaccard_similarity(get_alphabet_pairs(str1), get_alphabet_pairs(str2)))

def wrapper_solution(strs):
    return solution(strs[0], strs[1])

test_cases = [
    (["FRANCE", "french"], 16384),
    (["handshake", "shake hands"], 65536),
    (["aa1+aa2", "AAAA12"], 43690),
    (["E=M*C^2", "e=m*c^2"], 65536)
]

if __name__ == '__main__':
    tester = Tester(func=wrapper_solution)
    for case in test_cases:
        tester.run_test(input=case[0], output=case[1])
    tester.summary()