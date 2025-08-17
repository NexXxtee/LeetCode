# Нужно вывести максимальное число в отрезке массива 
# nums = [1, 3, 4, 5, 0, 0], k = 3, должно вернуть [4, 5, 5, 5]

# долгий алгоритм O(nk)
# def solution(nums: list[int], k: int):
#     left = 0
#     right = k
#     result = []

#     while right <= len(nums):
#         result.append(max(nums[left:right]))
#         left += 1
#         right += 1
    
#     return result


# print(solution([1, 3, 4, 5, 0, 0], 3))

from collections import deque


def solution(nums: list[int], k: int):
    left = 0
    right = k
    d = deque()
    result = []

    .