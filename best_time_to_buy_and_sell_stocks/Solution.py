class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1

        return maxProfit