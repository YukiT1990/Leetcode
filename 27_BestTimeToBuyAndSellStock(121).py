# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bestPriceToBuy = prices[0]
        for price in prices:
            if price < bestPriceToBuy:
                bestPriceToBuy = price
            elif price > bestPriceToBuy:
                profit = price - bestPriceToBuy
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit
