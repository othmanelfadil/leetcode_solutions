#BRUTE FORCE O(n^2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result =[0] * len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue 
                prod *= nums[j]
            result[i] = prod
        return result
        
        
#O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

