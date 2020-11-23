class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.", -2);
        String[] v2 = version2.split("\\.", 0);

        int places = (v1.length > v2.length) ? v1.length : v2.length;
        int[] v1_arr = new int[places];
        int[] v2_arr = new int[places];
        
        for (int i = 0; i < places; i++) {
            if (v1.length >= i + 1) v1_arr[i] = stripZero(v1[i]);
            else v1_arr[i] = 0;
            if (v2.length >= i + 1) v2_arr[i] = stripZero(v2[i]);
            else v2_arr[i] = 0;
        }

        return compare(v1_arr, v2_arr);
    }

    private int stripZero(String numSequence) {
        for (int i = 0; i < numSequence.length(); i++) {
            if (numSequence.charAt(i) != '0') {
                return Integer.parseInt(numSequence.substring(i));
            }
        }
        return 0;
    }

    private int compare(int[] arr1, int[] arr2) {
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] > arr2[i]) return 1;
            else if (arr1[i] < arr2[i]) return -1;
        }
        return 0;
    }

    private void printArr(int[] arr) {
        String str = "";
        for (int i : arr) {
            str += "'" + i + "' ";
        }
        System.out.println(str);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.compareVersion("1.01", "1.001") == 0;
        assert sol.compareVersion("1.0", "1.0.0") == 0;
        assert sol.compareVersion("0.1", "1.1") == -1;
        assert sol.compareVersion("1.0.1", "1") == 1;
        assert sol.compareVersion("7.5.2.4", "7.5.3") == -1;
    }
}