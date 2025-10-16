#BRUTE FORCE O(n log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#USING HASH MAP O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = {}
        for c in s: count[c] = count.get(c, 0) + 1
        for c in t:
            if c not in count: return False
            count[c] -= 1
            if count[c] == 0: del count[c]
        return not count
