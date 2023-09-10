package arrays_and_hashing.contains_duplicate;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class SolutionTest {
    private Solution solution;

    @BeforeEach
    void setUp() {
        solution = new Solution();
    }

    @ParameterizedTest
    @MethodSource
    void containsDuplicate(int[] input) {
        boolean result = solution.containsDuplicate(input);
        assertTrue(result);
    }
    static Stream<Arguments> containsDuplicate() {
        return Stream.of(
                Arguments.of(new int[]{1, 1}),
                Arguments.of(new int[]{1, 2, 1}),
                Arguments.of(new int[]{2, 3, 1, 1}),
                Arguments.of(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2})
        );
    }

    @ParameterizedTest
    @MethodSource
    void containsAllDistinct(int[] input) {
        var result = solution.containsDuplicate(input);
        assertFalse(result);
    }
    static Stream<Arguments> containsAllDistinct() {
        return Stream.of(
                Arguments.of(new int[]{1}),
                Arguments.of(new int[]{1, 2}),
                Arguments.of(new int[]{1, 2, 3})
        );
    }
}