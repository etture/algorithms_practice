from typing import List

class Solution:

    class Island(object):
        def __init__(self, block):
            self.coords = list()
            self.add_to_island(block)

        def includes(self, block):
            is_part = False
            # print(f'coords: {self.coords}')
            for x, y in block:
                if is_part:
                    break
                for coord_x, coord_y in self.coords:
                    # print(f'coords: ({coord_x}, {coord_y}), input: ({x}, {y})')
                    if x == coord_x and y == coord_y + 1:
                        is_part = True
                        break
                    elif x == coord_x + 1 and y == coord_y:
                        is_part = True
                        break
            # print(f'x: {x}, y: {y}, is_part: {is_part}')
            return is_part

        def add_to_island(self, block):
            for x_y in block:
                self.coords.append(x_y)

        def __repr__(self) -> str:
            return str(self.coords)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = list()
        for x, row in enumerate(grid):
            blocks = list()
            cur_block = list()
            create_new_block = True
            for y, item in enumerate(row):
                if create_new_block:
                    cur_block = list()
                if item == 0:
                    if len(cur_block) > 0:
                        blocks.append(cur_block)
                    create_new_block = True
                    continue
                else:
                    cur_block.append(tuple([x, y]))
                    create_new_block = False
                    if y == len(row) - 1:
                        blocks.append(cur_block)
            for block in blocks:
                is_part_of_existing = False
                for island in islands:
                    if island.includes(block):
                        island.add_to_island(block)
                        is_part_of_existing = True
                        break
                if not is_part_of_existing:
                    islands.append(self.Island(block))
        for i in islands:
            print(i)
        return len(islands)

if __name__ == '__main__':
    solution = Solution()
    input1 = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ] # 1
    input2 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ] # 3
    input3 = [
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1],
    ] # 5
    input4 = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1]
    ] # 2
    print(f'input: {input1}, output: {solution.numIslands(input1)}')
    print(f'input: {input2}, output: {solution.numIslands(input2)}')
    print(f'input: {input3}, output: {solution.numIslands(input3)}')
    print(f'input: {input4}, output: {solution.numIslands(input4)}')
