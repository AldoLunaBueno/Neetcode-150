package stack.largest_rect_histogram;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    Solution solution;
    @BeforeEach
    void setUp() {
        solution = new Solution();
    }
    @ParameterizedTest
    @MethodSource
    void testTrivial(int[] input, int expected) {
        int result = solution.largestRectangleArea(input);
        assertEquals(expected, result);
    }
    static Stream<Arguments> testTrivial() {
        return Stream.of(
                Arguments.of(new int[]{0}, 0),
                Arguments.of(new int[]{1}, 1),
                Arguments.of(new int[]{0, 1}, 1),
                Arguments.of(new int[]{1, 0}, 1),
                Arguments.of(new int[]{1, 1}, 2)
        );
    }
    @ParameterizedTest
    @MethodSource
    void testDrawnCases(int[] input, int expected) {
        int result = solution.largestRectangleArea(input);
        assertEquals(expected, result);
    }
    static Stream<Arguments> testDrawnCases() {
        return Stream.of(
                Arguments.of(new int[]{1, 2, 3, 4, 5, 6}, 12),
                Arguments.of(new int[]{6, 2, 1, 4, 3, 5}, 9),
                Arguments.of(new int[]{1, 4, 3, 2, 1, 5, 1}, 7),
                Arguments.of(new int[]{1, 3, 5, 2, 2}, 8)
        );
    }
}