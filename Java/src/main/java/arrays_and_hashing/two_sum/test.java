package arrays_and_hashing.two_sum;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public class test {
    public static void main(String[] args) {
        int[] arr = {2, 7, 11, 15};
        Integer[] arrInteger = Arrays.stream(arr)
                .boxed()
                .toArray(Integer[]::new);
        HashSet set = new HashSet<>(Arrays.asList(arrInteger));
        System.out.println("Set: " + set);
    }
}
