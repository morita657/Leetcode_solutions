import java.util.ArrayList;

class Solution {
    public int singleNumber(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int ind = nums[0];
        for (int i = 1; i < nums.length; i++) {
            ind ^= nums[i];
        }
        return ind;
    }
}