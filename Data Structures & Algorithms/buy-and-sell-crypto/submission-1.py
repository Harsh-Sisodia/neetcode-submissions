class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_cost = 1000

        for i in range(0,len(prices)):
            min_cost = min(min_cost,prices[i])
            profit = prices[i]-min_cost
            max_profit = max(max_profit,profit)
        return max_profit