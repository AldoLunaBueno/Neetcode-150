package arrays_and_hashing.contains_duplicate;

import java.util.HashSet;
import java.util.List;

public class Solution {
    boolean containsDuplicate(int[] nums) {
        HashSet set = new HashSet();
        for (int n :
                nums) {
            if (set.contains(n)) {
                return true;
            } else {
                set.add(n);
            }
        }
        return false;
    }
}
