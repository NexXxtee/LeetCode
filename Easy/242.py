# 242. Valid Anagram

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = defaultdict(int)

        for i in s:
            d[i] += 1

        for i in t:
            if d[i]:
                d[i] -= 1
            else:
                return False

        return True