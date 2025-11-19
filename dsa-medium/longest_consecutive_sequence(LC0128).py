# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for n in nset:
            if n-1 not in nset:
                lenght = 1
                while n + lenght in nset:
                    lenght += 1
                longest = max(lenght,longest)
            
        return longest