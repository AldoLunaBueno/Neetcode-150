class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers 'nums' and an integer 'target', 
        return indices of the two numbers such that they add up to 'target'.        
        """
        for i, x in enumerate(nums[:-1]):
            for j, y in enumerate(nums[i+1:]):
                if x + y == target:
                    return [i, 1+i+j]