# 49. Group Anagrams


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            d[s].append(strs[i])

        return [val for val in d.values()]