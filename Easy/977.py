# 977. Squares of a Sorted Array

# Нужно вернуть квадраты целых чисел отсортированного массива также в отсортированном виде
# [1, 2, 3, 4, 5]
# [-1, 0, 1, 2]
# [-5, -4, -3, 1, 4, 10]


def sortedSquares(nums):
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[right] ** 2)
                right -= 1
            else:
                result.append(nums[left] ** 2)
                left += 1

        return result[::-1]

print(sortedSquares([1, 2, 3, 4, 5]))
print(sortedSquares([-1, 0, 1, 2]))
print(sortedSquares([-5, -4, -3, 1, 4, 10]))