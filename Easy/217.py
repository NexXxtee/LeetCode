# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums) -> bool:
        d = set()

        for num in nums:
            if num in d:
                return True 
            d.add(num)

        return False

        