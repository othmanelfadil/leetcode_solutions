# O(n)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        if total % k == total:
            return total
        elif total % k == 0:
            return 0
        else:
            return total % k
        
# O(n)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q, r = divmod(sum(nums), k)
        return r