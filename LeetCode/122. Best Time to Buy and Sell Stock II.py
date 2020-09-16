class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        #Here we apply the greedy algorithm
        #Here even for keep raising condition, we can also take it as sell and buy on the same day.
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maximumProfit += prices[i] - prices[i-1]
        return maximumProfit
        
