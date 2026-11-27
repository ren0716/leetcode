class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        #unbounded knapsack problem
        #dp[i][j] is best item achievable using first i items with j budget, together with a 'used' array to track if i have used certain items
        #dp[i][j] = max(dp[i - 1][j - cost of current] + bonus, dp[i][j - cost of current] + 1)
        dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

        #check bonus for every item
        bonus = [] #bonus for item at index i
        for fp, _ in items:
            count = 0
            for ff, _ in items:
                if ff % fp == 0:
                    count += 1
            bonus.append(count)

        for i in range(1 ,len(items) + 1):
            cost, total = items[i - 1][1], bonus[i - 1]
            for j in range(0, budget + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= cost:
                    dp[i][j] = max(dp[i - 1][j - cost] + total, dp[i][j - cost] + 1, dp[i][j])
        return max(dp[len(items)])




        
        