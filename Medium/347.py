from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int):
    d = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]
    for num , freq in d.items():
        bucket[freq].append(num)
    
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))