class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers 'nums' and an integer 'target', 
        return indices of the two numbers such that they add up to 'target'.        
        """
        numsSet = set(nums)
        for x in numsSet:
            if target - x in numsSet:
                if x != target - x:
                    ind1 = nums.index(x)
                    ind2 = nums.index(target - x)                    
                else:
                    ind1 = nums.index(x)
                    nums.pop(ind1)
                    nums.insert(ind1, None)
                    try:
                        ind2 = nums.index(target - x)
                    except ValueError:
                        continue
                r = [ind1, ind2]
                r.sort()
                return r
