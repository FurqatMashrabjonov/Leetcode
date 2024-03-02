class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = max(profit, prices[r] - prices[l])
        
        return profit