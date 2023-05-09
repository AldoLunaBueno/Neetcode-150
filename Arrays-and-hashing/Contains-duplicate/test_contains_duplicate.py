import unittest
from contains_duplicate import *


class Test(unittest.TestCase):
    def test_contains_duplicate(self):
        lists = [
            [1, 1],
            [1, 2, 3, 1],
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        ]
        Test.assertContainsDuplicate(self, lists, True)

    def test_contains_distinct(self):
        lists = [
            [],
            [1],
            [1, 2],
            [1, 2, 3, 4]
        ]
        Test.assertContainsDuplicate(self, lists, False)
        """
        Refactorized:
        self.assertFalse(Solution.containsDuplicate(self, list00))
        self.assertFalse(Solution.containsDuplicate(self, list0))
        ...
        """
    def assertContainsDuplicate(self, lists, boolean):
        for nums in lists:
            self.assertEqual(Solution.containsDuplicate(self, nums), boolean)

if __name__=='__main__':
    unittest.main()