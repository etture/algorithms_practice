import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        final boolean USED = false;
        Set<List<Integer>> answers = new HashSet<>();
        for (int i = 0; i < nums.length - 2; i++) {
            int pivot = nums[i];
            int target = 0 - pivot;
            Map<Integer, Boolean> hashmap = new HashMap<>();
            for (int j = i + 1; j < nums.length; j++) {
                int curNum = nums[j];
                if (j == i + 1) {
                    hashmap.put(curNum, !USED);
                } else {
                    int complement = target - curNum;
                    if (hashmap.containsKey(complement) && hashmap.get(complement) != USED) {
                        hashmap.put(complement, USED);
                        hashmap.put(curNum, USED);
                        List<Integer> triplet = Arrays.asList(pivot, complement, curNum);
                        Collections.sort(triplet);
                        answers.add(triplet);
                    } else if (!hashmap.containsKey(curNum)) {
                        hashmap.put(curNum, !USED);
                    }
                }
            }
        }
        for (List<Integer> l : answers) {
            // System.out.println(l);
        }
        return new ArrayList<>(answers);
    }

    public static void main(String... args){
        Solution solution = new Solution();
        int[] input = new int[]{-1,0,1,2,-1,-4};
        List<List<Integer>> answer = solution.threeSum(input);
        System.out.println(answer);
        input = new int[]{0,0,0};
        answer = solution.threeSum(input);
        System.out.println(answer);
        input = new int[]{1,1,-2};
        answer = solution.threeSum(input);
        System.out.println(answer);
    }
}

