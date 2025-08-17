# 122. Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices) -> int:
        profit1 = 0
        profit2 = 0
        min_price = float("inf")

        for num in prices: 
            if num < min_price:
                min_price = num 
            if num - min_price > profit1:
                profit1 = num - min_price

        min_price = float("inf")
        for num in prices: 
            if num < min_price:
                min_price = num 
            if num - min_price > 0:
                profit2 += num - min_price
                min_price = float("inf")
                min_price = num 
                
        return max(profit1, profit2)
    

# Топ решение LeetCode '


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
        
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 profit += prices[i] - prices[i-1]
        
#         return profit