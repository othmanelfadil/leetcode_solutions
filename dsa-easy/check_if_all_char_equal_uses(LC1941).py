#O(n)
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occ = {}
        for c in s:
            occ[c] = occ.get(c,0) + 1
        return len(set(occ.values())) == 1