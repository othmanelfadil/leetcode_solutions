#HASH TABLE O(n*k) n is strings k is maximum string length
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map = {}
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        
        return list(hash_map.values())
    
#DIDN'T INCLUDE BRUTE FORCE SINCE WE ALREADY MADE THE VALID_ANAGRAM SOLUTION (and i was too lazy to think about it too :p)