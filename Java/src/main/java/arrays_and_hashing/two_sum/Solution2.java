package arrays_and_hashing.two_sum;

import java.util.HashSet;

public class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        HashSet set = new HashSet();
        for (int i = 0; i < nums.length; i++) {
            int x = target - nums[i];
            if (!set.contains(x))
                set.add(nums[i]);
            for (int j = 0; j < i; j++) {
                if (nums[j] == x)
                    return new int[]{j, i};
            }
        }
        return null;
    }
}
