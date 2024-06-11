class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            else:
                profit = max(profit, prices[i] - min_buy)
            
            
        return profit