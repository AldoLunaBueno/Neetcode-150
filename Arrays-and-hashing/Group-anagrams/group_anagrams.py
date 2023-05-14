from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list) # It's a wrapper: group["new key"] == [] (default)
        for s in strs:
            frec = [0] * 26 # english alphabet
            for c in s:
                c = ord(c) - ord("a") # char ascii position relative to "a"
                frec[c] += 1
            frec = tuple(frec)  # make frec hashable
            groups[frec].append(s)
        return list(groups.values())
