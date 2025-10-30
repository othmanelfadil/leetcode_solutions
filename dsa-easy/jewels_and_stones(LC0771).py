#O(whatever tf idc) n*m
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       sj = {}  

       for stone in stones:
        if stone in jewels:
            sj[stone] = sj.get(stone, 0) + 1
       return sum(sj.values())
