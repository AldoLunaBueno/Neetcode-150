import pytest
from valid_palindrome import *

sol = Solution()

class Test:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ("", True),
            ("a", True), ("A", True), ("0", True),
            (" ,-#)?%", True)
        ])
    def test_trivial_success(self, input, expected):
        assert sol.isPalindrome(input) == expected

    @pytest.mark.parametrize(
        "input, expected",
        [
            ("aa", True), ("aA", True),
            (" a", True), (",a", True),
            ("ab", False), ("aB", False), ("00", True),
            ("0P", False) # ord("P") - ord("0") = ord("a") - ord("A") = 32
        ])
    def test_two_chars(self, input, expected):
        assert sol.isPalindrome(input) == expected

    @pytest.mark.parametrize(
        "input, expected",
        [
            ("aaa", True), ("aba", True), ("101", True), ("a0a", True),
            ("a,a", True),
            ("abb", False)
        ])
    def test_three_chars(self, input, expected):
        assert sol.isPalindrome(input) == expected

    @pytest.mark.parametrize(
        "input, expected",
        [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False)
        ])
    def test_more_chars(self, input, expected):
        assert sol.isPalindrome(input) == expected


if __name__ == "__main__":
    pytest.main()
