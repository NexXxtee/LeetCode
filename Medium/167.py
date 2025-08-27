# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers, target: int):
        l = 0
        r = len(numbers) - 1

        while l <= r:
            current = numbers[l] + numbers[r]

            if current > target:
                r -= 1
            elif current < target: 
                l += 1
            else:
                return [l + 1, r + 1]