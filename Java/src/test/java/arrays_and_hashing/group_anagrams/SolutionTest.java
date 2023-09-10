package arrays_and_hashing.group_anagrams;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.not;

class SolutionTest {
    @ParameterizedTest
    @MethodSource
    void testOk(Integer[] arr1, Integer[] arr2) {
        assertThat(Arrays.asList(arr1))
                .containsExactlyInAnyOrderElementsOf(Arrays.asList(arr2));
    }
    static Stream<Arguments> testOk() {
        return Stream.of(
                Arguments.of(new Integer[]{1}, new Integer[]{1}),
                Arguments.of(new Integer[]{1, 2}, new Integer[]{2, 1}),
                Arguments.of(new Integer[]{1, 2, 3, 3}, new Integer[]{3, 2, 1, 3})
        );
    }

    @ParameterizedTest
    @MethodSource
    void testFail(Integer[] arr1, Integer[] arr2) {
        assertThat(Collections.singleton(Arrays.asList(arr1))).noneSatisfy(
                candidate ->
                        assertThat(candidate)
                                .containsExactlyInAnyOrderElementsOf(Arrays.asList(arr2))
        );
    }

    static Stream<Arguments> testFail() {
        return Stream.of(
                Arguments.of(new Integer[]{1}, new Integer[]{2}),
                Arguments.of(new Integer[]{1, 2, 2}, new Integer[]{1, 1, 2}),
                Arguments.of(new Integer[]{1, 1, 2, 2, 3, 3}, new Integer[]{1, 2, 3, 3, 3, 3})
        );
    }


}