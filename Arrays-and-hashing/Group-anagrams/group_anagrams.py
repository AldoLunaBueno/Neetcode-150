class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = []
        groupDict = {}
        for str in strs:
            frec = {}
            for c in str:
                if c in frec:
                    frec[c] += 1
                else:
                    frec[c] = 1
            frec = tuple(sorted(frec.items())) # make frec hashable
            index = groupDict.get(frec)
            if index is None:
                index = len(groups)
                groups.append([])                
                groupDict[frec] = index           
            groups[index].append(str)
        return groups