class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers 'nums' and an integer 'target', 
        return indices of the two numbers such that they add up to 'target'.        
        """        
        nums = sorted(enumerate(nums), key= lambda x: x[1])
        for i in nums:
            for j in nums[::-1]:
                if i[1] + j[1] < target:
                    break
                elif i[1] + j[1] > target:
                    continue
                else:
                    r = [i[0], j[0]]
                    r.sort()
                    return r

# print(Solution.twoSum(Solution, [-2, 1, 6, 7], 4))

