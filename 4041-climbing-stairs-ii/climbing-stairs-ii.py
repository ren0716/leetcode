class Solution:

    #step 01234
    #cost 1234
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        costs.insert(0, 0)
        for i in range(1, n + 1):
            #choose lowest from previous 3 
            for j in range(i - 3, i):
                if j >= 0:
                    dp[i] = min(dp[i], costs[i] + (i - j) * (i - j) + dp[j])
        return dp[n]
        
        