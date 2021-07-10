# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        priceToBuy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - priceToBuy
            if profit > 0:
                totalProfit += profit
                priceToBuy = prices[i]
            else:
                priceToBuy = min(prices[i], priceToBuy)
        return totalProfit
