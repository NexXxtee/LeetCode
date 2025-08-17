# 13. Roman to Integer

def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        s = s[::-1]
        result = 0
        temp = s[0]

        for num in s:
            if nums[temp] <= nums[num]:
                result += nums[num]
                temp = num 
            else:
                result -= nums[num]
                temp = num 

        return result 
                