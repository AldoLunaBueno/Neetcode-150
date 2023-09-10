package arrays_and_hashing.two_sum;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

class SolutionTest {
    Solution solution;

    @BeforeEach
    void setUp() {
        solution =new Solution();
    }

    @ParameterizedTest
    @MethodSource
    void trivialSum(int[] nums, int target, int[] expected) {
        int[] result = solution.twoSum(nums, target);
        Assertions.assertArrayEquals(expected, result);
    }

    static Stream<Arguments> trivialSum() {
        return Stream.of(
                Arguments.of(new int[]{2,7,11,15}, 9, new int[]{0,1}),
                Arguments.of(new int[]{3,2,4}, 6, new int[]{1, 2}),
                Arguments.of(new int[]{3, 3}, 6, new int[]{0, 1})
        );
    }

}