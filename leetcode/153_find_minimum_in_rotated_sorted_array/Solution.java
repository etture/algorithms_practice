class Solution {
    public int findMin(int[] nums) {
        // linear
        // int min = nums[0];
        // for (int num : nums) {
        //     if (num < min) {
        //         return num;
        //     }
        // }
        // return min;

        // binary search
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return nums[0] < nums[1] ? nums[0] : nums[1];
        if (nums[0] < nums[nums.length - 1]) return nums[0];

        int midIdx = Math.floorDiv(nums.length, 2);
        int leftMinIdx = 0;
        int rightMaxIdx = nums.length - 1;
        while (nums[midIdx] < nums[midIdx + 1] && nums[midIdx - 1] < nums[midIdx]) {
            if (nums[midIdx] > nums[0]) { // go right
                leftMinIdx = midIdx;
                midIdx = Math.floorDiv(midIdx + rightMaxIdx, 2);
            } else {
                rightMaxIdx = midIdx;
                midIdx = Math.floorDiv(midIdx + leftMinIdx, 2);
            }
        }
        if (nums[midIdx] > nums[midIdx + 1]) {
            return nums[midIdx + 1];
        } else {
            return nums[midIdx];
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.findMin(new int[]{1, 2, 3, 4, 0}) == 0;
    }
}