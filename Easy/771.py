# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        count = 0
        for i in jewels:
            d[i] = 0 

        for i in stones: 
            if i in d:
                count += 1

        return count 