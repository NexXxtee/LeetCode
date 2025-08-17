# 2239. Find Closest Number to Zero

def findClosestNumber(nums) -> int:
        min = 10 ** 5 + 1
        for i in nums:
            if abs(i) < abs(min):
                min = i
            elif abs(i) == abs(min) and i > 0:
                min = i
        return min