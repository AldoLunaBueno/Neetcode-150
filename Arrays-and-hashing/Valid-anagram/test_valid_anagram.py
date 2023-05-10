from valid_anagram import *
import unittest

class Test(unittest.TestCase):
    def test_is_anagram(self):        
        self.assertTrue(Solution.isAnagram(self, "", ""))
        self.assertTrue(Solution.isAnagram(self, "a", "a"))
        self.assertTrue(Solution.isAnagram(self, "ab", "ba"))
        self.assertTrue(Solution.isAnagram(self, "aaaab", "baaaa"))
        self.assertTrue(Solution.isAnagram(self, "abcda", "aabcd"))
    def test_is_not_anagram(self):
        self.assertFalse(Solution.isAnagram(self, "", "a"))
        self.assertFalse(Solution.isAnagram(self, "a", "aa"))
        self.assertFalse(Solution.isAnagram(self, "a", "b"))
        self.assertFalse(Solution.isAnagram(self, "ab", "ca"))
        self.assertFalse(Solution.isAnagram(self, "aaaab", "aaaaa"))
        self.assertFalse(Solution.isAnagram(self, "abcda", "abcdd"))
if __name__=='__main__':
    unittest.main()