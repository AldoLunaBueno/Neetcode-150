package stack.valid_parentheses;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
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
    void testIsValid(String input) {
        boolean result = solution.isValid(input);
        assertTrue(result);
    }

    static Stream<Arguments> testIsValid() {
        return Stream.of(
                Arguments.of("()"),
                Arguments.of("[]"),
                Arguments.of("{}"),
                Arguments.of("()[]{}"),
                Arguments.of("([])"),
                Arguments.of("()[{}]"),
                Arguments.of("{[]{()}}[]")
        );
    }

    @ParameterizedTest
    @MethodSource
    void testIsNotValid(String input) {
        boolean result = solution.isValid(input);
        assertFalse(result);
    }

    static Stream<Arguments> testIsNotValid() {
        return Stream.of(
                Arguments.of("("),
                Arguments.of(")"),
                Arguments.of("[["),
                Arguments.of("}}"),
                Arguments.of("(]"),
                Arguments.of("([)"),
                Arguments.of("([)]"),
                Arguments.of("[{}]([{])")
        );
    }
}
