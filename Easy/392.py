# 392. Is Subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        p1 = p2 = 0
        
        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                count += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        return count == len(s)