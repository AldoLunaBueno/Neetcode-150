class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, 
        and return false if every element is distinct.
        """
        hashset = set()
        for x in nums:            
            if x in hashset:
                return True
            hashset.add(x)
        return False
