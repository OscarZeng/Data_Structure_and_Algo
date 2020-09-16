class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowerestPrice = float(inf)
        maximumProfit = 0
        #We go through the list and check record the minimal price and keep updating the maximum profit
        for i in prices:
            lowerestPrice = min(i, lowerestPrice)
            maximumProfit = max(i - lowerestPrice, maximumProfit)
        return maximumProfit