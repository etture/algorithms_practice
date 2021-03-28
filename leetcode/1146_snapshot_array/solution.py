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



class SnapshotArrayWithLinkedList:
    
    class LinkedListNode:
        def __init__(self, snap_id: int, val: int):
            self.snap_id = snap_id
            self.val = val
            self.prev = None

        def get_val_at_snap_id(self, snap_id: int) -> int:
            if snap_id >= self.snap_id:
                return self.val
            else:
                return self.prev.get_val_at_snap_id(snap_id)


    def __init__(self, length: int):
        self.array = [0] * length
        self.snap_id = -1
        self.snapshots_map = dict()
        self.changed_before_snapshot = list()
        for idx, val in enumerate(self.array):
            self.snapshots_map[idx] = self.LinkedListNode(self.snap_id, val)

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        self.changed_before_snapshot.append(index)

    def snap(self) -> int:
        self.snap_id += 1
        for idx in self.changed_before_snapshot:
            new_node = self.LinkedListNode(self.snap_id, self.array[idx])
            new_node.prev = self.snapshots_map[idx]
            self.snapshots_map[idx] = new_node
        self.changed_before_snapshot = list()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        # pp.pprint(self.snapshots_map)
        return self.snapshots_map[index].get_val_at_snap_id(snap_id)


class SnapshotArray:
    
    class IndexSnapshotNode:
        def __init__(self, snap_id, val):
            self.snap_id_list = [snap_id]
            self.snap_val_map = {snap_id: val}

        def add_new_snapshot(self, snap_id, val):
            self.snap_id_list.append(snap_id)
            self.snap_val_map[snap_id] = val
            # print(self.snap_val_map)

        def get_val_at_snap_id(self, snap_id: int) -> int:
            if snap_id in self.snap_id_list:
                return self.snap_val_map[snap_id]
            else:
                # find closest snap_id with binary search
                right_snap_id = self._find_snap_id(snap_id)
                return self.snap_val_map[right_snap_id]

        def _find_snap_id(self, snap_id: int) -> int:
            def condition(idx) -> str:
                if snap_id == self.snap_id_list[idx]:
                    return 'good'
                elif idx+1 < len(self.snap_id_list) and snap_id > self.snap_id_list[idx+1]:
                    return 'right'  # go right
                elif idx-1 >= 0 and self.snap_id_list[idx] > snap_id:
                    return 'left'  # go left
                else:
                    return 'good'
            left, right = 0, len(self.snap_id_list)-1
            middle = (left + right) // 2
            while left <= right:
                # print(f'  while loop, left: {left}, right: {right}, middle: {middle}')
                check = condition(middle)
                if check == 'good':
                    # print(f'       _find_snap_id() -> snap_id_list: {self.snap_id_list}, snap_val_map: {self.snap_val_map}, snap_id: {snap_id}, middle: {middle}, returned_snap_id: {self.snap_id_list[middle]}')
                    return self.snap_id_list[middle]
                elif check == 'right':
                    left = middle + 1
                elif check == 'left':
                    right = middle - 1
                middle = (left + right) // 2
                

                
    def __init__(self, length: int):
        self.array = [0] * length
        self.snap_id = -1
        self.snapshots_map = dict()
        self.changed_before_snapshot = set()
        for idx, val in enumerate(self.array):
            self.snapshots_map[idx] = self.IndexSnapshotNode(self.snap_id, val)

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        self.changed_before_snapshot.add(index)

    def snap(self) -> int:
        self.snap_id += 1
        for idx in self.changed_before_snapshot:
            self.snapshots_map[idx].add_new_snapshot(self.snap_id, self.array[idx])
        self.changed_before_snapshot = set()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots_map[index].get_val_at_snap_id(snap_id)



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

class Solution:
    def run(self, commands: List[str], params: List[List[int]]) -> List[int]:
        answer = list()
        for i in range(len(commands)):
            command = commands[i]
            param = params[i]
            if command == "SnapshotArray":
                obj = SnapshotArray(param[0])
                answer.append(None)
            elif command == "set":
                answer.append(obj.set(*param))
            elif command == "snap":
                answer.append(obj.snap())
            elif command == "get":
                answer.append(obj.get(*param))
        return answer


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [
                ["SnapshotArray", "set", "snap", "set", "get"],
                [[3], [0, 5], [], [0, 6], [0, 0]]
            ],
            [None,None,0,None,5]
        ),
        (
            [
                ["SnapshotArray", "set", "set", "snap", "set", "get", "set", "set", "snap", "get", "snap", "set", "get", "snap", "get"],
                [[10], [0, 5], [3, 10], [], [1, 6], [1, 0], [0, 19], [3, 12], [], [3, 1], [], [3, 222], [3, 2], [], [3, 3]]
            ],
            # [19,6,0,222,0,0,0,0,0,0]
            # 0 -> [5,0,0,10,0,0,0,0,0,0]
            # 1 -> [19,6,0,12,0,0,0,0,0,0]
            # 2 -> [19,6,0,12,0,0,0,0,0,0]
            # 3 -> [19,6,0,222,0,0,0,0,0,0]
            [None,None,None,0,None,0,None,None,1,12,2,None,12,3,222]
        ),
        (
            [
                ["SnapshotArray","snap","snap","set","snap","get","set","get","snap","get"],
                [[1],[],[],[0,4],[],[0,1],[0,12],[0,1],[],[0,3]]
            ],
            [None,0,1,None,2,0,None,0,3,12]
        ),
        (
            [
                ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"],
                [[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
            ],
            [None,None,0,1,2,15,3,4,15]
        ),
        (
            [
                ["SnapshotArray","snap","get","get","set","snap","set","get","set","snap","get","set","set"],
                [[1],[],[0,0],[0,0],[0,2],[],[0,14],[0,1],[0,12],[],[0,0],[0,17],[0,16]]
            ],
            [None,0,0,0,None,1,None,2,None,2,0,None,None]
        )
    ]

    Tester.factory(test_cases, func=lambda input: sol.run(*input)).run(unordered_output=False)
