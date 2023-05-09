import unittest
from contains_duplicate import *

class Test(unittest.TestCase):
    def test_contains_duplicate(self):
        list1 = [1, 1]
        list2 = [1,2,3,1]
        list3 = [1,1,1,3,3,4,3,2,4,2]
        self.assertTrue(Solution.containsDuplicate(self, list1))
        self.assertTrue(Solution.containsDuplicate(self, list2))
        self.assertTrue(Solution.containsDuplicate(self, list3))
    def test_contains_distinct(self):
        list00 = []
        list0 = [1]
        list1 = [1, 2]
        list2 = [1,2,3,4]
        self.assertFalse(Solution.containsDuplicate(self, list00))
        self.assertFalse(Solution.containsDuplicate(self, list0))
        self.assertFalse(Solution.containsDuplicate(self, list1))
        self.assertFalse(Solution.containsDuplicate(self, list2))