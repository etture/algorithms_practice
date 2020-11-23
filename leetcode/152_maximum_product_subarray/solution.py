from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd = list(), list()
        for idx, num in enumerate(nums):
            if idx == 0:
                maxProd.append(num)
                minProd.append(num)
            else:
                candidates = [minProd[idx-1]*num, num, maxProd[idx-1]*num]
                maxProd.append(max(candidates))
                minProd.append(min(candidates))
        print(maxProd)
        print(minProd)
        return max(maxProd)


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([2, 3, -2, 4, 5]) == 20
    assert sol.maxProduct([4, -10, -2, 3, -4, 7]) == 240
    assert sol.maxProduct([-2, 0, -1]) == 0
