#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            profit = prices[i] - min

            if profit > max_profit:
                max_profit = profit
        
        if max_profit == 0: return 0
        else: return max_profit