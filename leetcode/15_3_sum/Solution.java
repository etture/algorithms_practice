import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();

        Arrays.sort(nums);

        // System.out.println(Arrays.toString(nums));

        if (nums.length < 3) return answer;

        for (int i = 0; i < nums.length - 2; i++) {
            int curNum = nums[i];
            int complement = -curNum;
            if (i == 0 && curNum > 0) return answer;
            if (i > 0 && curNum == nums[i-1]) continue;
            Map<Integer, Boolean> curSet = new HashMap<>();
            for (int j = i + 1; j < nums.length; j++) {
                int iterNum = nums[j];
                if (j == i + 1) {
                    curSet.put(iterNum, false);
                    continue;
                } else if (curSet.containsKey(complement - iterNum) && !curSet.get(complement - iterNum).booleanValue()) {
                    curSet.put(complement - iterNum, true);
                    answer.add(Arrays.asList(curNum, complement - iterNum, iterNum));
                }
                if (!curSet.containsKey(iterNum)) {
                    curSet.put(iterNum, false);
                }
            }
        }
        
        // System.out.println(answer.toString());

        return answer;
    }

    public static void main(String... args){
        Solution solution = new Solution();
        int[] input = new int[]{-1,0,1,2,-1,-4};
        List<List<Integer>> answer = solution.threeSum(input);
        // System.out.println(answer);
        input = new int[]{0,0,0};
        answer = solution.threeSum(input);
        // System.out.println(answer);
        input = new int[]{1,1,-2};
        answer = solution.threeSum(input);
        // System.out.println(answer);
    }
}

