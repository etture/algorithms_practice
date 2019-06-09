from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        final_nums = []

        nums1.reverse()
        nums2.reverse()
        while len(final_nums) < ((total_length // 2) + 1):
            print(f'final_nums: {final_nums}')
            if len(nums1) == 0:
                final_nums.append(nums2.pop())
            elif len(nums2) == 0:
                final_nums.append(nums1.pop())
            elif nums1[-1] <= nums2[-1]:
                final_nums.append(nums1.pop())
            else:
                final_nums.append(nums2.pop())

        # Odd
        if total_length % 2 == 1:
            return float(final_nums[-1])
        # Even
        else:
            return float((final_nums[-1] + final_nums[-2]) / 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
