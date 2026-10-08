class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minp = prices[0]
        for i in prices:
            minp = min(minp,i)
            currp = i-minp
            if currp>0:
                ans+=currp
                minp=i
        return (ans)
        