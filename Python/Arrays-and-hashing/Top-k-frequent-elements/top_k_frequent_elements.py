class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
        Given an integer array 'nums' and an integer 'k', 
        return the 'k' most frequent elements in any order.
        '''
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        maxFreq = max(freq.values())
        bucket = [[] for i in range(maxFreq+1)]
        for key, v in freq.items():
            bucket[v].append(key)

        res = []
        for l in bucket[::-1]:
            if len(res) < k:
                res.extend(l)
            else:
                break
        return res[:k]
            
