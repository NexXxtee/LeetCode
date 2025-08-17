# 1. Two Sum

class Solution:
    def twoSum(self, nums, target: int):
        d = dict()

        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in d and d[curr] != i:
                return [i, d[curr]]
            d[nums[i]] = i

        return []
