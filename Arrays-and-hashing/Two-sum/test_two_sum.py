import unittest
from two_sum import *

class Test(unittest.TestCase):
    def test_trivial(self):
        result = Solution.twoSum(self, [1, 2], 3)
        self.assertEqual(result, [0, 1])
        result = Solution.twoSum(self, [0, 1, 2], 3)
        self.assertEqual(result, [1, 2])

    def test_use_distincts(self):
        result = Solution.twoSum(self, [1, 1], 2)
        self.assertEqual(result, [0, 1])
        result = Solution.twoSum(self, [4, 1, 2, 3], 4)
        self.assertEqual(result, [1, 3])

    def test_negatives(self):
        result = Solution.twoSum(self, [-2, 1, 6, 7], 4)
        self.assertEqual(result, [0, 2])
        result = Solution.twoSum(self, [-2, -1, 5, -2], -4)
        self.assertEqual(result, [0, 3])

if __name__== '__main__':
    unittest.main()
