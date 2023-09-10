package arrays_and_hashing.test_tool;

import java.util.Arrays;
import java.util.Comparator;

public class TestTool {
    void assertArrayEqualIgnoredOrder() {
        Integer[] a1 = {1, 1, 2, 2, 3, 3};
        Integer[] a2 = {1, 2, 3, 3, 3, 3};
        System.out.println(Arrays.asList(a1));
    }

    public static void main(String[] args) {
        new TestTool().assertArrayEqualIgnoredOrder();
    }
}
