# O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying = prices[0]
        profit = 0

        for price in prices[1:]:
            if buying > price:
                buying = price
            profit = max(profit, price - buying)
        return profit