class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit(2, [2,4,1]) == 2
    assert sol.maxProfit(2, [3,2,6,5,0,3]) == 7
    assert sol.maxProfit(1, [1, 5, 2, 8, 3, 11, 2, 15, 4, 3, 4, 9, 20]) == 19
    assert sol.maxProfit(2, [1, 5, 2, 8, 3, 11, 2, 15, 4, 3, 4, 9, 20]) == 31
    assert sol.maxProfit(3, [1, 5, 2, 8, 3, 11, 2, 15, 4, 3, 4, 9, 20]) == 19
