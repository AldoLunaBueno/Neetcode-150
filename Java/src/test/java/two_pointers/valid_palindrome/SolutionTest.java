package two_pointers.valid_palindrome;

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
    void testTrivialSuccess(String input) {
        boolean result = solution.isPalindrome(input);
        assertTrue(result);
    }
    static Stream<Arguments> testTrivialSuccess() {
        return Stream.of(
                Arguments.of(" "),
                Arguments.of("a"),
                Arguments.of("A"),
                Arguments.of("0"),
                Arguments.of("a ,-#)?%")
        );
    }

    @ParameterizedTest
    @MethodSource
    void testTwoCharsSuccess(String input) {
        boolean result = solution.isPalindrome(input);
        assertTrue(result);
    }
    static Stream<Arguments> testTwoCharsSuccess() {
        return Stream.of(
                Arguments.of("aa"),
                Arguments.of("aA"),
                Arguments.of(" a"),
                Arguments.of(",a"),
                Arguments.of("00")
        );
    }

    @ParameterizedTest
    @MethodSource
    void testTwoCharsFail(String input) {
        boolean result = solution.isPalindrome(input);
        assertFalse(result);
    }
    static Stream<Arguments> testTwoCharsFail() {
        return Stream.of(
                Arguments.of("ab"),
                Arguments.of("aB"),
                Arguments.of("0P") // ord("P") - ord("0") = ord("a") - ord("A") = 32
        );
    }

    @ParameterizedTest
    @MethodSource
    void testThreeCharsSuccess(String input) {
        boolean result = solution.isPalindrome(input);
        assertTrue(result);
    }
    static Stream<Arguments> testThreeCharsSuccess() {
        return Stream.of(
                Arguments.of("aaa"),
                Arguments.of("aba"),
                Arguments.of("101"),
                Arguments.of("a0a"),
                Arguments.of("aa,")
        );
    }

    @ParameterizedTest
    @MethodSource
    void testMoreChars(String input, boolean expected) {
        boolean result = solution.isPalindrome(input);
        assertEquals(expected, result);
    }
    static Stream<Arguments> testMoreChars() {
        return Stream.of(
                Arguments.of("A man, a plan, a canal: Panama", true),
                Arguments.of("race a car", false)
        );
    }
}