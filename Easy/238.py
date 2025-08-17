# 238. Product of Array Except Self

def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        left = 1
        right = 1

        for i in range(len(nums)):
            j = (i + 1) * (-1)
            answer[i] *= left
            left *= nums[i]
            answer[j] *= right
            right *= nums[j]
            
        return answer