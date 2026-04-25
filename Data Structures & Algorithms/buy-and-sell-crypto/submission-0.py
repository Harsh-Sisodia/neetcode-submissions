class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(0,len(prices)):
            profit = 0
            for j in range(i+1,len(prices)):
                profit = prices[j]-prices[i]
                max_profit = max(max_profit,profit)
        
        return max_profit