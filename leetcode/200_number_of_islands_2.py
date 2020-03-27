from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        class Node:
            def __init__(self, coords, sequence, x_len, y_len):
                self.x, self.y = coords
                self.sequence = sequence
                self.x_len, self.y_len = x_len, y_len
            
            def search(self):
                all_included_nodes = set([(self.x, self.y)])
                self.sequence.append((self.x, self.y))
                x_forward_nodes, x_backward_nodes = set(), set()
                y_forward_nodes, y_backward_nodes = set(), set()
                print(f'x, y: ({self.x}, {self.y}), x_len: {self.x_len}, y_len: {self.y_len}')
                if self.x + 1 < self.x_len \
                        and (self.x + 1, self.y) not in self.sequence \
                        and grid[self.x + 1][self.y] == '1':
                    next_node = Node(
                        (self.x + 1, self.y), self.sequence, self.x_len, self.y_len)
                    x_forward_nodes = next_node.search()
                if self.x - 1 >= 0 \
                        and (self.x - 1, self.y) not in self.sequence \
                        and grid[self.x - 1][self.y] == '1':
                    next_node = Node(
                        (self.x - 1, self.y), self.sequence, self.x_len, self.y_len)
                    x_backward_nodes = next_node.search()
                if self.y + 1 < self.y_len \
                        and (self.x, self.y + 1) not in self.sequence \
                        and grid[self.x][self.y + 1] == '1':
                    next_node = Node(
                        (self.x, self.y + 1), self.sequence, self.x_len, self.y_len)
                    y_forward_nodes = next_node.search()
                if self.y - 1 >= 0 \
                        and (self.x, self.y - 1) not in self.sequence \
                        and grid[self.x][self.y - 1] == '1':
                    next_node = Node(
                        (self.x, self.y - 1), self.sequence, self.x_len, self.y_len)
                    y_backward_nodes = next_node.search()
                print(f'--end ({self.x}, {self.y}), x_forward: {x_forward_nodes}, x_backward: {x_backward_nodes}, y_forward: {y_forward_nodes}, y_backward: {y_backward_nodes}')
                print(f'searched: {all_included_nodes | x_forward_nodes | x_backward_nodes | y_forward_nodes | y_backward_nodes}')
                return all_included_nodes | x_forward_nodes | x_backward_nodes | y_forward_nodes | y_backward_nodes

        already_included = set()
        islands = list()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '0':
                    continue
                if (x, y) in already_included:
                    continue
                print(f'({(x, y)}, new start)')
                node = Node((x, y), list(), len(grid), len(grid[0]))
                island = node.search()
                islands.append(island)
                already_included = already_included | island
        # for i in islands:
        #     print(sorted(list(i)))
            # print(list(i))
        return len(islands)

if __name__ == '__main__':
    solution = Solution()
    input1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ] # 1
    input2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ] # 3
    input3 = [
        ['1', '0', '1', '0', '1'],
        ['1', '1', '0', '1', '1'],
        ['0', '0', '1', '0', '1'],
        ['1', '1', '1', '0', '0'],
        ['1', '0', '0', '1', '1'],
    ] # 5
    input4 = [
        ['1', '0', '1', '1', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '1', '1', '0', '1'],
    ] # 1
    input5 = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"],
    ] # 1
    print(f'input: {input1}, output: {solution.numIslands(input1)}')
    print(f'input: {input2}, output: {solution.numIslands(input2)}')
    print(f'input: {input3}, output: {solution.numIslands(input3)}')
    print(f'input: {input4}, output: {solution.numIslands(input4)}')
    print(f'input: {input5}, output: {solution.numIslands(input5)}')
