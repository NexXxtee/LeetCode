# 383. Ransom Note

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        d = defaultdict(int)

        for i in magazine:
            d[i] += 1

        for i in ransomNote:
            if d[i]:
                d[i] -= 1
            else:
                return False

        return True
