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
    def numIslands_bad(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid) > 0 and len(grid[0]) == 0:
            return 0

        height = len(grid)
        width = len(grid[0])
        marking_grid = [[0] * width for h in range(height)]

        island_cnt = 0

        for h, row in enumerate(grid):
            for w, elem in enumerate(row):
                # print(f'h: {h}, w: {w}, row: {row}, elem: {elem}')
                if elem == "1": # land
                    cur_island = marking_grid[h][w]
                    # print(f'    elem=="1", cur_island: {cur_island}')
                    if cur_island == 0: # not marked as part of any island
                        if w + 1 < width and marking_grid[h][w+1] > 0:
                            cur_island = marking_grid[h][w+1]
                        else:
                            island_cnt += 1
                            cur_island = island_cnt
                            # print(f'        new island: {cur_island}')
                        marking_grid[h][w] = cur_island
                    if w + 1 < width:
                        if grid[h][w+1] == "1": # land
                            marking_grid[h][w+1] = cur_island
                    # if w - 1 >= 0:
                    #     if grid[h][w-1] == "1": # land
                    #         marking_grid[h][w-1] = cur_island
                    if h + 1 < height:
                        if grid[h+1][w] == "1": # land
                            marking_grid[h+1][w] = cur_island
                    # if h - 1 >= 0:
                    #     if grid[h-1][w] == "1": # land
                    #         marking_grid[h-1][w] = cur_island
        # from pprint import pprint
        # pprint(marking_grid)
        return island_cnt
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid) > 0 and len(grid[0]) == 0:
            return 0

        SEA, LAND = "0", "1"
        height = len(grid)
        width = len(grid[0])
        mark_grid = [[0] * width for _ in range(height)]

        def dfs(grid: List[List[str]]) -> int:
            def _dfs(h: int, w: int, island_num: int) -> None:
                if 0<=h<height and 0<=w<width \
                        and mark_grid[h][w] == 0 and grid[h][w] == LAND:
                    mark_grid[h][w] = island_num
                    _dfs(h+1, w, island_num)
                    _dfs(h-1, w, island_num)
                    _dfs(h, w+1, island_num)
                    _dfs(h, w-1, island_num)

            island_cnt = 0
            for h, row in enumerate(grid):
                for w, elem in enumerate(row):
                    if elem == LAND:
                        if mark_grid[h][w] > 0:
                            continue
                        else:
                            island_cnt += 1
                            _dfs(h, w, island_cnt)
            # print(mark_grid)
            return island_cnt

        def bfs(grid: List[List[str]]) -> int:
            from collections import deque

            def _bfs(h: int, w: int, island_num: int) -> None:
                queue = deque([(h, w)])
                while queue:
                    h_, w_ = queue.popleft()
                    if 0<=h_<height and 0<=w_<width \
                            and mark_grid[h_][w_] == 0 and grid[h_][w_] == LAND:
                        mark_grid[h_][w_] = island_num
                        queue.append((h_+1, w_))
                        queue.append((h_-1, w_))
                        queue.append((h_, w_+1))
                        queue.append((h_, w_-1))
            
            island_cnt = 0
            for h, row in enumerate(grid):
                for w, elem in enumerate(row):
                    if elem == LAND:
                        if mark_grid[h][w] > 0:
                            continue
                        else:
                            island_cnt += 1
                            _bfs(h, w, island_cnt)
            return island_cnt

        return bfs(grid)


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    (
        [
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
        ],
        1
    ),
    (
        [
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
        ],
        3
    ),
    (
        [
            [
                ["0","1","0"],
                ["1","0","1"],
                ["0","1","0"]
            ]
        ],
        4
    ),
    (
        [
            [
                ["1","1","1"],
                ["0","1","0"],
                ["1","1","1"]
            ]
        ],
        1
    ),
    (
        [
            [
                ["1","0","1","1","1"],
                ["1","0","1","0","1"],
                ["1","1","1","0","1"]
            ]
        ],
        1
    )
]

solution = Solution().numIslands

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
