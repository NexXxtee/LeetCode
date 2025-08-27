# 128. Longest Consecutive Sequence


class Solution:
    def longestConsecutive(self, nums) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1  not in s:
                count = 1 
                next_number = num + 1
                while next_number in s:
                    count += 1
                    next_number += 1
                longest = max(longest, count)

        return longest 
                