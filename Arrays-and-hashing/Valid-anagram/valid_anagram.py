class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        
        s = Solution.strToDict(s)
        t = Solution.strToDict(t)
        if s == t:
            return True
        return False
    def strToDict(s: str) -> dict:
        sDict = {}
        for e in list(s):
            if e in sDict:                
                sDict[e] += 1
            else:
                sDict[e] = 1
        return sDict
    