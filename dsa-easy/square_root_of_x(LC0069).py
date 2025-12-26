# O(logn)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 1, x
        while l <= r:
            inter = (l + r) // 2
            if inter * inter == x:
                return inter
            elif inter * inter < x:
                l = inter + 1
            else:
                r = inter - 1
        return r