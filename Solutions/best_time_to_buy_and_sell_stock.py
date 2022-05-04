class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimum = prices[0]
        profit = 0
        
        
        for i in range(len(prices)):
            profit = prices[i]-minimum
            minimum = min(prices[i], minimum)
            maximum = max(profit, maximum)
            
        return maximum