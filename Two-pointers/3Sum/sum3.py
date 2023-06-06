class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)        
        res = set()
        n = len(nums)
        for k in range(n-2):
            if k>0 and nums[k] == nums[k-1]:
                continue
            i, j = k+1, n-1
            # Two sum
            target = -nums[k]
            while i < j:
                twoSum = nums[i] + nums[j]
                if twoSum < target:
                    i += 1
                elif twoSum > target:
                    j += -1
                else:
                    res.add((nums[k], nums[i], nums[j]))
                    i += 1
        # Tuples to arrays
        res = [[*tup] for tup in res]
        return res