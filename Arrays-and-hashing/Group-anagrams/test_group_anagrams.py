import unittest
from group_anagrams import Solution as sol
from deepdiff import DeepDiff

class Test(unittest.TestCase):
    def test_trivial_grouping(self):
        arranges = [[""],   ["a"],   ["a", "a"]]
        expected = [[[""]], [["a"]], [["a", "a"]]]
        results = [sol.groupAnagrams(self, arrange) for arrange in arranges]
        Test.assertEqualIgnoringOrder(self, results, expected)

    def test_one_group(self):
        arranges = [["ab", "ba"],   ["bab", "abb", "bba"]]        
        expected = [[["ab", "ba"]], [["abb", "bab", "bba"]]]
        results = [sol.groupAnagrams(self, arrange) for arrange in arranges]
        Test.assertEqualIgnoringOrder(self, results, expected)

    def test_two_groups(self):
        arranges = [["", "a"],     ["ab", "ba", "ac", "ca"],     ["abb", "bab", "baa"]]
        expected = [[[""], ["a"]], [["ab", "ba"], ["ac", "ca"]], [["abb", "bab"], ["baa"]]]
        results = [sol.groupAnagrams(self, arrange) for arrange in arranges]
        Test.assertEqualIgnoringOrder(self, results, expected)

    def test_more_groups(self):
        arranges = [["eat", "tea", "tan", "ate", "nat", "bat"]]
        expected = [[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]]
        results = [sol.groupAnagrams(self, arrange) for arrange in arranges]
        Test.assertEqualIgnoringOrder(self, results, expected)

    def assertEqualIgnoringOrder(self, results: list[str], expected: list[str]):
        for i, result in enumerate(results):
            self.assertEqual(DeepDiff(result, expected[i], ignore_order=True), {})

if __name__=='__main__':
    unittest.main()
