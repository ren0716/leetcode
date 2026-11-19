class Solution:
    def integerBreak(self, n: int) -> int:
        #dp[i] will be the max achievable product when n = i
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [float('-inf')] * (n + 1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[j] * dp[i - j], dp[i])
        return dp[n]

        