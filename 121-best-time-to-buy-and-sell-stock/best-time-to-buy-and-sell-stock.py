class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        mx = 0

        for sell in prices:
            profit = sell - buy
            mx = max(profit, mx)
            if sell < buy:
                buy = sell

        return mx 

        
        
        
        