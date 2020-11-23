import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int maxProduct(int[] nums) {
        int length = nums.length;
        Integer[] maxProd = new Integer[length];
        Integer[] minProd = new Integer[length];
        for (int i = 0; i < length; i++) {
            if (i == 0) {
                maxProd[i] = nums[i];
                minProd[i] = nums[i];
            } else {
                Integer[] candidates = {minProd[i-1]*nums[i], nums[i], maxProd[i-1]*nums[i]};
                maxProd[i] = Collections.max(Arrays.asList(candidates));
                minProd[i] = Collections.min(Arrays.asList(candidates));
            }
        }
        // printList(maxProd);
        // printList(minProd);
        return Collections.max(Arrays.asList(maxProd));
    }

    void printList(Integer[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.printf("%d ", arr[i]);
        }
        System.out.println("");
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.maxProduct(new int[]{2, 3, -2, 4}) == 6;
        assert sol.maxProduct(new int[]{2, 3, -2, 4, 5}) == 20;
        assert sol.maxProduct(new int[]{4, -10, -2, 3, -4, 7}) == 240;
        assert sol.maxProduct(new int[]{-2, 0, -1}) == 0;
    }
}
