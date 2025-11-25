# O(n)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum = n * (n + 1) // 2
        div3 = 0
        for i in range (m, n + 1 , m):
            div3 += i
        return (sum - div3) - div3
        