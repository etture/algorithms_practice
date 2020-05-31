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
logger = Logger(verbose=True)                             
# ----------------------------------------------------------

class Solution:
    def totalFruit_timeout(self, tree: List[int]) -> int:
        max_fruits = 0
        for start_idx in range(0, len(tree)):
            fruit_types = set([tree[start_idx]])
            cnt = 0
            for end_idx in range(start_idx, len(tree)):
                fruit = tree[end_idx]
                if fruit in fruit_types:
                    cnt += 1
                elif len(fruit_types) == 1:
                    cnt += 1
                    fruit_types.add(fruit)
                else:
                    # logger.log(f'tree[{start_idx}:{end_idx}]: {tree[start_idx:end_idx]} -> cnt: {cnt}')
                    break
            if cnt > max_fruits:
                max_fruits = cnt
        return max_fruits

    def totalFruit_timeout2(self, tree: List[int]) -> int:
        max_fruits = 0
        for start_idx in range(0, len(tree)):
            start_fruit = tree[start_idx]
            if start_idx > 0 and start_fruit == tree[start_idx-1]:
                continue
            fruit_types = set([tree[start_idx]])
            cnt = 0
            for end_idx in range(start_idx, len(tree)):
                next_fruit = tree[end_idx]
                if next_fruit in fruit_types:
                    cnt += 1
                elif len(fruit_types) == 1:
                    cnt += 1
                    fruit_types.add(next_fruit)
                else:
                    # logger.log(f'tree[{start_idx}:{end_idx}]: {tree[start_idx:end_idx]} -> cnt: {cnt}')
                    break
            if cnt > max_fruits:
                max_fruits = cnt
        return max_fruits

    def totalFruit(self, tree: List[int]) -> int:
        fruit_cnts = list()
        cur_fruit = -1
        cur_cnt = 0
        for idx, fruit in enumerate(tree):
            if fruit == cur_fruit:
                cur_cnt += 1
            else:
                if idx > 0:
                    fruit_cnts.append({'type': cur_fruit, 'cnt': cur_cnt})
                cur_fruit = fruit
                cur_cnt = 1
            if idx == len(tree)-1:
                fruit_cnts.append({'type': cur_fruit, 'cnt': cur_cnt})
        logger.log(fruit_cnts)

        fruit_types = list()
        max_cnt = 0
        cur_cnt = 0
        for idx, f in enumerate(fruit_cnts):
            if len(fruit_types) < 2:
                fruit_types.append(f['type'])
                cur_cnt += f['cnt']
            elif f['type'] in fruit_types:
                fruit_types.pop(0)
                fruit_types.append(f['type'])
                cur_cnt += f['cnt']
            else:
                fruit_types.pop(0)
                fruit_types.append(f['type'])
                cur_cnt = fruit_cnts[idx-1]['cnt']
                cur_cnt += f['cnt']
            if cur_cnt > max_cnt:
                max_cnt = cur_cnt
            logger.log(f'idx: {idx}, f: {f}, fruit_types: {fruit_types}, cur_cnt: {cur_cnt}, max_cnt: {max_cnt}')
        
        return max_cnt

'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output
test_cases = [
    ([[1,2,1]], 3),
    ([[0,1,2,2]], 3),
    ([[1,2,3,2,2]], 4),
    ([[3,3,3,1,2,1,1,2,3,3,4]], 5),
    ([[1,0,1,4,1,4,1,2,3]], 5),
]

solution = Solution().totalFruit

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
