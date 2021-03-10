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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:  # Just recursive DFS
        if len(grid) == 0: return 0

        row_len = len(grid)
        col_len = len(grid[0])
        
        seen = set()
        max_area = 0

        def traverse(x: int, y: int) -> int:
            area = 0
            if grid[x][y] == 1 and tuple([x, y]) not in seen:
                seen.add(tuple([x, y]))
                area += 1
                for direction in [-1, 1]:
                    if x + direction < row_len and x + direction >= 0:
                        area += traverse(x+direction, y)
                    if y + direction < col_len and y + direction >= 0:
                        area += traverse(x, y+direction)
            return area

        for r_idx, row in enumerate(grid):
            for c_idx, cur in enumerate(row):
                if cur == 1 and tuple([r_idx, c_idx]) not in seen:
                    max_area = max(max_area, traverse(r_idx, c_idx))

        return max_area


    class Island:
        def __init__(self, coord: tuple[int, int] = None):
            self.coordinates = set()
            if coord:
                self.coordinates.add(coord)

        def add(self, coord: tuple[int, int]):
            self.coordinates.add(coord)

        def merge(self, other: Solution.Island):
            self.coordinates.update(other.coordinates)

        def get_area(self) -> int:
            return len(self.coordinates)

        def __repr__(self) -> str:
            return f'<Island area={self.get_area()}, coordinates={self.coordinates}'


    def maxAreaOfIsland_usingIsland(self, grid: List[List[int]]) -> int:
        if len(grid) < 1:
            return 0
        row_cnt = len(grid)
        col_cnt = len(grid[0])

        coord_island_map = dict()
        unique_islands = list()

        for r_idx, row in enumerate(grid):
            for c_idx, cur in enumerate(row):
                if cur == 0:
                    continue
                elif cur == 1:
                    coord = tuple([r_idx, c_idx])
                    if coord not in coord_island_map:
                        coord_island_map[coord] = self.Island(coord)
                        unique_islands.append(coord_island_map[coord])
                    island = coord_island_map[coord]

                    # look right
                    if c_idx + 1 < col_cnt and grid[r_idx][c_idx+1] == 1:
                        right_coord = tuple([r_idx, c_idx+1])
                        if right_coord not in coord_island_map:
                            island.add(right_coord)
                            coord_island_map[right_coord] = island
                        else:
                            right_island = coord_island_map[right_coord]
                            if island is not right_island:
                                island.merge(right_island)
                                coord_island_map[right_coord] = island
                                for inner_coord in right_island.coordinates:
                                    coord_island_map[inner_coord] = island

                    # look left
                    # if c_idx - 1 >= 0 and grid[r_idx][c_idx-1] == 1:
                    #     left_coord = tuple([r_idx, c_idx-1])
                    #     if left_coord not in coord_island_map:
                    #         island.add(left_coord)
                    #         coord_island_map[left_coord] = island

                    # look down
                    if r_idx + 1 < row_cnt and grid[r_idx+1][c_idx]:
                        down_coord = tuple([r_idx+1, c_idx])
                        if down_coord not in coord_island_map:
                            island.add(down_coord)
                            coord_island_map[down_coord] = island
                        else:
                            down_island = coord_island_map[down_coord]
                            if island is not down_island:
                                island.merge(down_island)
                                coord_island_map[down_coord] = island
                                for inner_coord in down_island.coordinates:
                                    coord_island_map[inner_coord] = island

                    # look up
                    # if r_idx - 1 < row_cnt and grid[r_idx-1][c_idx]:
                    #     up_coord = tuple([r_idx-1, c_idx])
                    #     if up_coord not in coord_island_map:
                    #         island.add(up_coord)
                    #         coord_island_map[up_coord] = island

        print(unique_islands)
        return max([island.get_area() for island in unique_islands]) if len(unique_islands) > 0 else 0
        

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[0,0,0,0,0,0,0,0]]], 0),
        ([
           [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        ], 6),
        ([
           [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        ], 12),
        ([
           [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,1],
            [0,1,1,0,1,0,0,0,0,0,0,0,1],
            [0,1,0,0,1,1,0,0,1,0,1,0,1],
            [0,1,0,0,1,1,0,0,1,0,1,0,1],
            [0,0,0,0,0,0,0,0,0,0,1,0,1],
            [0,0,0,0,0,0,0,1,1,0,1,0,1],
            [0,0,0,0,0,0,0,1,1,0,0,0,1]]
        ], 7),
        ([
           [[0,1,1],
            [1,1,1]]
        ], 5),
        ([
           [[1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0],
            [1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,0],
            [0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0],
            [1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1],
            [0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1]]
        ], 18)
    ]

    Tester.factory(test_cases, func=lambda input: sol.maxAreaOfIsland(*input)).run(unordered_output=False)
