from typing import List

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        v1_list, v2_list = list(), list()
        places = 0
        if len(v1) > len(v2):
            places = len(v1)
        else:
            places = len(v2)
        
        for idx in range(places):
            if len(v1) >= idx + 1:
                v1_list.append(self.strip_zero(v1[idx]))
            else:
                v1_list.append(0)

            if len(v2) >= idx + 1:
                v2_list.append(self.strip_zero(v2[idx]))
            else:
                v2_list.append(0)

        return self.compare(v1_list, v2_list)

    def strip_zero(self, num_sequence: str) -> int:
        for idx, char in enumerate(num_sequence):
            if char != '0':
                return int(num_sequence[idx:])
        return 0

    def compare(self, list1: List[int], list2: List[int]) -> int:
        # print(f'list1: {list1}, list2: {list2}')
        for idx in range(len(list1)):
            if list1[idx] > list2[idx]:
                return 1
            elif list1[idx] < list2[idx]:
                return -1
        return 0



if __name__ == '__main__':
    sol = Solution()
    assert sol.compareVersion("1.01", "1.001") == 0
    assert sol.compareVersion("1.0", "1.0.0") == 0
    assert sol.compareVersion("0.1", "1.1") == -1
    assert sol.compareVersion("1.0.1", "1") == 1
    assert sol.compareVersion("7.5.2.4", "7.5.3") == -1
