#BRUTE FORCE O(n^2)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i

#USING A SET O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

#OPTIMAL SOLUTION USING ARITHEMETIC SUM O(1)* 
# *space complexity
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # 0 + 1 + 2......+ n = (n x (n + 1)) / 2
        expected_sum = n * (n + 1) // 2 #// is an integer division no remainder
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    

#XOR APPROACH (BITWISE XOR) O(1)*
# *space complexity
# see more https://allen.in/jee/physics/exclusive-or-gate
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)  # start with n
        # let's take [3, 0, 1] as our array
        # XOR all indices and numbers 3 ^ 0 ^ 3 = 0 -> 0 ^ 1 ^ 0 = 1 -> 1 ^ 2 ^ 1 = 2 (^ is the bitwise operator for XOR in python) 
        # leaving only the missing number at the end in this case it is 2 !
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing