class Solution {
    public int myAtoi(String s) {
        boolean signRead = false;
        boolean digitRead = false;
        boolean isNegative = false;
        String numStr = "";
        for (int idx = 0; idx < s.length(); idx++) {
            char ch = s.charAt(idx);
            if (!signRead && !digitRead) {
                if (ch == ' ') continue;
                else if (ch == '-') {
                    signRead = true;
                    isNegative = true;
                }
                else if (ch == '+') {
                    signRead = true;
                }
                else if (Character.isDigit(ch)) {
                    signRead = true;
                    digitRead = true;
                    numStr += ch;
                }
                else return 0;
            }
            else if (signRead && !digitRead) {
                if (!Character.isDigit(ch)) return 0;
                else {
                    digitRead = true;
                    numStr += ch;
                }
            }
            else {
                if (!Character.isDigit(ch)) break;
                else numStr += ch;
            }
        }
        int numLength = numStr.length();
        long numInt = 0;
        for (int i = 0; i < numLength; i++) {
            int numCandidate = Character.getNumericValue(numStr.charAt(i));
            // System.out.println("numCandidate = " + numCandidate);
            numInt += numCandidate * Math.pow(10, numLength - 1 - i);
            // System.out.println("numInt = " + numInt);
        }
        // System.out.println(numStr);
        // System.out.println("isNegative: " + isNegative);
        // System.out.println(numInt);
        if (isNegative) {
            numInt = -numInt;
            // System.out.println("numInt = " + numInt);
            if (numInt < (int) -Math.pow(2, 31)) return (int) -Math.pow(2, 31);
            return (int) numInt;
        } else {
            if (numInt > (int) Math.pow(2, 31)) return (int) Math.pow(2, 31);
            // System.out.println((int)-Math.pow(2,31));
            return (int) numInt;
        }

    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.myAtoi("42") == 42;
        assert sol.myAtoi("-42") == -42;
        assert sol.myAtoi("4193 with words") == 4193;
        assert sol.myAtoi("words and 987") == 0;
        assert sol.myAtoi("-91283472332") == -2147483648;
        // System.out.println("answer: " + sol.myAtoi("21474836460"));
        assert sol.myAtoi("21474836460") == 2147483647;
    }
}