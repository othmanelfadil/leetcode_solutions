class Solution:
    def countBits(self, n: int) -> List[int]:
        bc = [0] * (n + 1)
        r = 1

        for i in range(1, n + 1):
            if r * 2 == i:
                r = i
            bc[i] = bc[i - r] + 1
        
        return bc