from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # for ind, num in enumerate(nums):
        #     for internal_ind, internal_num in enumerate(nums):
        #         if ind == internal_ind:
        #             continue
        #         else:
        #             if num + internal_num == target:
        #                 return list([ind, internal_ind])

        # hashing
        nums_dict = defaultdict(lambda: tuple((0, 0)))

        for ind, num in enumerate(nums):
            nums_dict[num] = tuple((ind, 1))

        for ind, num in enumerate(nums):
            complement = target - num
            if nums_dict[complement][1] == 1 and nums_dict[complement][0] != ind:
                return [ind, nums_dict[complement][0]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3,2,4], 6))
