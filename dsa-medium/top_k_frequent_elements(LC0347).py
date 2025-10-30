#BRUTE FORCE O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] = count.get(n, 0) + 1
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [x for x, _ in sorted_items[:k]]


#BUCKET SORT O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for _ in range(len(nums)+1)]
        for num, c in count.items():
            freq[c].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):  
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                