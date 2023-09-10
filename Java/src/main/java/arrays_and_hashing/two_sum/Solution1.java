package arrays_and_hashing.two_sum;

import java.util.Arrays;
import java.util.HashSet;

public class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        Integer[] numsIntegers = Arrays.stream(nums)
                .boxed()
                .toArray(Integer[]::new);
        HashSet set = new HashSet<>(Arrays.asList(numsIntegers));

        for (int i = 0; i < nums.length; i++) {
            int x = target - nums[i];

            if (!set.contains(x))
                continue;

            for (int j = 1; j < nums.length; j++) {
                if (nums[j] == x && i != j)
                    return new int[]{i, j};
            }
        }
        return null;
    }
}
