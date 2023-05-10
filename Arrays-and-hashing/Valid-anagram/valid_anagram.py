class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        
        sDict = Solution.strToDict(s)
        tDict = Solution.strToDict(t)
        if sDict == tDict:
            return True
        return False
    def strToDict(s: str) -> dict:
        sDict = {}
        for e in s:
            sDict[e] = 1 + sDict.get(e, 0)
        return sDict