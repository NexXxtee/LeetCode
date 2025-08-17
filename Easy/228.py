# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return nums
            
        result = []
        i = 1
        temp = [nums[0]]

        while i < len(nums):
            if nums[i] - 1 == nums[i - 1]:
                temp.append(nums[i])
            else:
                if len(temp) > 1:
                    result.append(f"{temp[0]}->{temp[-1]}")
                    
                else:
                    result.append(f"{temp[0]}")
                    
                temp = []
                temp.append(nums[i])
            i += 1

        if len(temp) > 1:
            result.append(f"{temp[0]}->{temp[-1]}")
            
        else:
            result.append(f"{temp[0]}")
            
        return result 
                
            
            