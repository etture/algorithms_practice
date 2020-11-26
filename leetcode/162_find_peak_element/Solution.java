import java.util.Arrays;

class Solution {
    public int findPeakElement(int[] nums) {
        // linear
        // int prev = -999999999;
        // for (int i = 0; i < nums.length; i++) {
        //     if ((i-1 >= 0 && nums[i] > nums[i-1]) || i-1 < 0) {
        //         if ((i+1 <= nums.length-1 && nums[i] > nums[i+1]) || i+1 >= nums.length) {
        //             System.out.println(i);
        //             return i;
        //         }
        //     }
        // }
        // return -1;

        // logarithmic
        int floor = 0;
        int ceiling = nums.length - 1;
        int midIdx = Math.floorDiv(ceiling + floor, 2);

        while (true) {
            boolean leftIsLower = true;
            boolean rightIsLower = true;

            if (midIdx != 0 && nums[midIdx] <= nums[midIdx-1]) leftIsLower = false;
            if (midIdx != nums.length - 1 && nums[midIdx] <= nums[midIdx+1]) rightIsLower = false;

            if (leftIsLower && rightIsLower) {
                // System.out.println(midIdx);
                return midIdx;
            }
            
            if (!leftIsLower) { // left is higher, go left
                ceiling = midIdx;
                if (midIdx - floor <= 1) midIdx = floor;
                else midIdx = Math.floorDiv(midIdx + floor, 2);
            } else { // right is higher, go right
                floor = midIdx;
                if (ceiling - midIdx <= 1) midIdx = ceiling;
                else midIdx = Math.floorDiv(midIdx + ceiling, 2);
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.findPeakElement(new int[]{1,2,3,1}) == 2;
        assert Arrays.asList(1, 5).contains(sol.findPeakElement(new int[]{1,2,1,3,5,6,4}));
        assert sol.findPeakElement(new int[]{-123123123}) == 0;
        assert sol.findPeakElement(new int[] {1,2,3,4,5,6,7,8,9,10,11,12}) == 11;
        assert sol.findPeakElement(new int[]{13,12,11,10,9,8,7,6,5,4,3,2,1,0}) == 0;
    }
}