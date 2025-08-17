# 392. Is Subsequence

from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = {}