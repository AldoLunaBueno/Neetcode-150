import unittest
from valid_palindrome import *
from parameterized import parameterized

class Test(unittest.TestCase):
    @parameterized.expand([
        ("", True), 
        ("a", True), ("A", True), ("0", True), 
        (" ,-#)?%", True)
    ])
    def test_trivial_success(self, input, expected):
        Test.assertEqual(self, input, expected)
    
    @parameterized.expand([
        ("aa", True), ("aA", True),
        (" a", True), ("a,", True)
        ("ab", False), ("aB", False), ("00", True)
    ])
    def test_two_chars(self, input, expected):
        Test.assertEqual(self, input, expected)

    @parameterized.expand([
        ("aaa", True), ("aba", True), ("101", True), ("a0a", True),
        ("a,a", True),
        ("abb", False)
    ])
    def test_three_chars(self, input, expected):
        Test.assertEqual(self, input, expected)

    @parameterized.expand([
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False)
    ])
    def test_more_chars(self, input, expected):
        Test.assertEqual(self, input, expected)
if __name__=="__main__":
    unittest.main()