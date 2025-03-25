from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                max_profit = profit if profit > max_profit else max_profit
        return max_profit
    

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))