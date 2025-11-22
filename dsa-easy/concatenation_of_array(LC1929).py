# O(n)
def getConcatenation(self, nums: List[int]) -> List[int]:
        l = 2 * len(nums)
        ans = [0] * l
        for i in range(len(nums)):
                ans[i] = nums[i]
                ans[i + (l // 2)] = nums[i]
        return ans

# O(n) 
# don't be an idiot this is the easiest way
def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

# or this one

def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums