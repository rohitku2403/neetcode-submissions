class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            a = min(a,prices[i])
            max_profit = max(max_profit,prices[i]-a)
        return max_profit
        
        