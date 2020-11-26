from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # linear
        # prev = -9999999999
        # for idx, num in enumerate(nums):
        #     if (idx > 0 and num > prev) or idx == 0:
        #         if idx >= len(nums) - 1 or num > nums[idx+1]:
        #             return idx

        #     prev = num

        # logarithmic
        if len(nums) == 1:
            return 0
        
        mid_idx = len(nums) // 2
        floor = 0
        ceiling = len(nums) - 1

        while True:
            left_is_lower, right_is_lower = True, True
            mid_num = nums[mid_idx]
            if mid_idx - 1 >= 0 and nums[mid_idx - 1] >= mid_num:
                left_is_lower = False
            if mid_idx + 1 <= len(nums) - 1 and mid_num <= nums[mid_idx + 1]:
                right_is_lower = False

            # print(f'mid_idx: {mid_idx}, mid_num: {mid_num}, left_is_lower: {left_is_lower}, right_is_lower: {right_is_lower}, floor: {floor}, ceiling: {ceiling}')

            if left_is_lower and right_is_lower:
                return mid_idx
            else:
                if not left_is_lower: # left is higher, go left
                    ceiling = mid_idx
                    if mid_idx - floor <= 1:
                        mid_idx = floor
                    else:
                        mid_idx = (mid_idx + floor) // 2
                else: # right is higher, go right
                    floor = mid_idx
                    if ceiling - mid_idx <= 1:
                        mid_idx = ceiling
                    else:
                        mid_idx = (mid_idx + ceiling) // 2


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findPeakElement([13,12,11,10,9,8,7,6,5,4,3,2,1,0]))
    assert sol.findPeakElement([1,2,3,1]) == 2
    assert sol.findPeakElement([1,2,1,3,5,6,4]) in (1, 5)
    assert sol.findPeakElement([-123123123]) == 0
    assert sol.findPeakElement([1,2,3,4,5,6,7,8,9,10,11,12]) == 11
    assert sol.findPeakElement([13,12,11,10,9,8,7,6,5,4,3,2,1,0]) == 0
