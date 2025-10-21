class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] == nums [j]: 
                    return True 
        return False



# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)