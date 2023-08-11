// brute force
class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        for (int i = 0; i < prices.length; ++i) {
            int buyPrice = prices[i];
            for (int j = i + 1; j < prices.length; ++j) {
                int sellPrice = prices[j];
                int profit = sellPrice - buyPrice;
                if (profit > max) {
                    max = profit;
                }
            }
        }
        return max;
    }
}

// optimized
class Solution {
    public int maxProfit(int[] prices) {
        int leastPrice = Integer.MAX_VALUE;
        int overallProfit = 0;
        int todayProfit = 0;
        
        for (int i = 0; i < prices.length; ++i) {
            if (prices[i] < leastPrice) {
                leastPrice = prices[i];
            }
            todayProfit = prices[i] - leastPrice;
            if (todayProfit > overallProfit) {
                overallProfit = todayProfit;
            }
        }
        return overallProfit;
    }
}