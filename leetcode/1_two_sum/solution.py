from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one-pass hash table
        hash_table = dict()
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hash_table and hash_table[complement] != idx:
                return [hash_table[complement], idx]
            hash_table[num] = idx
        

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [0, 1]
    assert sol.twoSum([3,2,4], 6) == [1, 2]
    assert sol.twoSum([3,3], 6) == [0, 1]
