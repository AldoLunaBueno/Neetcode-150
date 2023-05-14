class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
        Given an integer array 'nums' and an integer 'k', 
        return the 'k' most frequent elements in any order.
        '''
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        res = []
        for i in range(k):
            t = max(freq, key = lambda x: freq[x])
            freq.pop(t)
            res.append(t)
        return res
            
