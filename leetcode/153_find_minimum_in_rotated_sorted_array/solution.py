from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # naive
        # min_num = nums[0]
        # for num in nums:
        #     if num < min_num:
        #         min_num = num
        # return min_num

        # optimized
        # min_num = nums[0]
        # prev_num = nums[0]
        # for idx, num in enumerate(nums):
        #     if idx > 0 and num < prev_num:
        #         return num
        #     if num < min_num:
        #         min_num = num
        #     prev_num = num
        # return min_num

        # binary search
        # [2,4,5,6,7,0,1]
        # [3, 4, 1], [3, 1, 2]
        # [2, 3, 4, 5, 1]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]

        mid_idx = len(nums) // 2
        left_min_idx = 0
        right_max_idx = len(nums) - 1
        while nums[mid_idx] < nums[mid_idx + 1] and nums[mid_idx - 1] < nums[mid_idx]:
            print(f'mid_idx: {mid_idx}, num: {nums[mid_idx]}, left_min_idx: {left_min_idx}, right_max_idx: {right_max_idx}')
            if nums[mid_idx] > nums[0]: # go right
                left_min_idx = mid_idx
                mid_idx = (mid_idx + right_max_idx) // 2
                print(f'    go right, new mid_idx: {mid_idx}')
            else: # go left
                right_max_idx = mid_idx
                mid_idx = (mid_idx + left_min_idx) // 2
                print(f'    go left, new mid_idx: {mid_idx}')
        if nums[mid_idx] > nums[mid_idx + 1]:
            return nums[mid_idx + 1]
        else:
            return nums[mid_idx]
        
if __name__ == '__main__':
    sol = Solution()
    input = [284,287,289,293,295,298,0,3,8,9,10,11,12,15,17,19,20,22,26,29,30,31,35,36,37,38,42,43,45,50,51,54,56,58,59,60,62,63,68,70,73,74,81,83,84,87,92,95,99,101,102,105,108,109,112,114,115,116,122,125,126,127,129,132,134,136,137,138,139,147,149,152,153,154,155,159,160,161,163,164,165,166,168,169,171,172,174,176,177,180,187,188,190,191,192,198,200,203,204,206,207,209,210,212,214,216,221,224,227,228,229,230,233,235,237,241,242,243,244,246,248,252,253,255,257,259,260,261,262,265,266,268,269,270,271,272,273,277,279,281]
    print(sol.findMin(input))
