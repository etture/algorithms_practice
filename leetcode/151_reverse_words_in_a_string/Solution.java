import java.util.*;

class Solution {
    public String reverseWords(String s) {
        String[] tokens = s.trim().split("\\s+");
        return String.join(" ", reverseStringArray(tokens));
    }

    List<String> reverseStringArray(String[] arr) {
        int len = arr.length;
        List<String> list = new ArrayList<>();
        for (int i = len-1; i >= 0; i--) {
            list.add(arr[i]);
        }
        return list;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverseWords("the sky is blue"));
        System.out.println(sol.reverseWords("a good   example"));
        System.out.println(sol.reverseWords("  hello world  "));
        System.out.println(sol.reverseWords("  Bob    Loves  Alice   "));
    }
}
