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

        # Reference
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/803206/Python-O(n)-by-DP-w-Visualization

        # # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        # cur_hold, cur_not_hold = -float('inf'), 0
        
        # for stock_price in prices:
            
        #     prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
		# 	# either keep hold, or buy in stock today at stock price
        #     cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
		# 	# either keep not-hold, or sell out stock today at stock price
        #     cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        # # maximum profit must be in not-hold state
        # return cur_not_hold if prices else 0
    
    
        # profit_from_price_gain = 0
        # for idx in range( len(prices)-1 ):
            
        #     if prices[idx] < prices[idx+1]:
        #         profit_from_price_gain += ( prices[idx+1] - prices[idx])
                
        # return profit_from_price_gain
