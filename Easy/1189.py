# 1189. Maximum Number of Balloons

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = 'balloon'
        c = Counter(text)
        counter = 0

        while True:
            for i in balloon:
                if c[i]:
                    c[i] -= 1
                else:
                    return counter 

            counter += 1

        return counter 
        