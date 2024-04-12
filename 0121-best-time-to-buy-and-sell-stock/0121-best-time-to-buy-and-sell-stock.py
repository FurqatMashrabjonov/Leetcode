class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        l, r = 0, 0
        
        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            
            if prices[r] < prices[l]:
                l = r
            
            r += 1
        
        return profit