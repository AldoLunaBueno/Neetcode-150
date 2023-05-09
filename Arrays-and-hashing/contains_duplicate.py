import unittest
from ast import List

class Solution:
    def containsDuplicate(self, nums: List(int)) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, 
        and return false if every element is distinct.
        """
        for i, x in enumerate(nums[:-1]):
            for y in nums[i+1:]:
                if x == y:
                    return True
        return False