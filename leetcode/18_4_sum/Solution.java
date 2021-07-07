import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        // System.out.println("\n" + Arrays.toString(nums));

        List<List<Integer>> answer = new ArrayList<>();

        // FOURSUM
        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int firstNum = nums[i];
            int firstComplement = target - firstNum;

            // THREESUM
            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) {
                    continue;
                }
                int secondNum = nums[j];
                int secondComplement = firstComplement - secondNum;
                
                // TWOSUM
                Map<Integer, Boolean> seen = new HashMap<>();
                for (int k = j + 1; k < nums.length; k++) {
                    int thirdNum = nums[k];
                    int thirdComplement = secondComplement - thirdNum;

                    if (k > j + 1 && seen.containsKey(thirdComplement) && !seen.get(thirdComplement).booleanValue()) {
                        // System.out.println("i: " + i + ", j: " + j + ", k: " + k + ", thirdNum: " + thirdNum + ", thirdComplement: " + thirdComplement + ", seen[thirdComplement]: " + seen.get(thirdComplement));
                        // match
                        answer.add(List.of(firstNum, secondNum, thirdComplement, thirdNum));
                        seen.put(thirdComplement, true);
                    }
                    if (!seen.containsKey(thirdNum)) seen.put(thirdNum, false);
                }
            }
        }
        return answer;
    }

    public static void main(String... args){
        Solution solution = new Solution();
        int[] input = new int[]{1,0,-1,0,-2,2};
        int target = 0;
        List<List<Integer>> answer = solution.fourSum(input, target);
        System.out.println(answer);
        input = new int[]{2,2,2,2,2};
        target = 8;
        answer = solution.fourSum(input, target);
        System.out.println(answer);
        input = new int[]{0,2,2,2,10,-3,-9,2,-10,-4,-9,-2,2,8,7};
        target = 6;
        answer = solution.fourSum(input, target);
        System.out.println(answer);
    }
}