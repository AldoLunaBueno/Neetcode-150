package arrays_and_hashing.valid_anagram;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertTrue;

class SolutionTest {
    private Solution solution;
    @BeforeEach
    void setUp() {
        solution = new Solution();
    }

    @ParameterizedTest
    @MethodSource
    void testIsAnagram(String s, String t) {
        boolean result = solution.isAnagram(s, t);
        assertTrue(result);
    }
    static Stream<Arguments> testIsAnagram() {
        return Stream.of(
                Arguments.of("a", "a"),
                Arguments.of("aa", "aa"),
                Arguments.of("ab", "ab"),
                Arguments.of("aaab", "baaa"),
                Arguments.of("abcda", "aabcd")
        );
    }

    @ParameterizedTest
    @MethodSource
    void testIsNotAnagram(String s, String t) {
    }
    static Stream<Arguments> testIsNotAnagram() {
        return Stream.of(
                Arguments.of("a", "b"),
                Arguments.of("a", "aa"),
                Arguments.of("ab", "ac"),
                Arguments.of("aaab", "aaaa"),
                Arguments.of("aabc", "abcc")
        );
    }
}