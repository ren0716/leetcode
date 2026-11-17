class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        #dp[i][j] as partition dp where it stands for the min steps needed to change the string s ending at i into j valid parts
        #we can precompute v[i][j] where its the cost of change s[i][j] to a semi-palidrome
        #transition -> dp[i][j] = min(dp[x][j - 1] + v[x + 1][i])

        #build v[i][j]
        n = len(s)
        INF = float("inf")
       # cost[i][j] is for the half-open substring s[i:j]
        cost = [[INF] * (n + 1) for _ in range(n + 1)]

        for left in range(n):
            for right in range(left + 2, n + 1):
                length = right - left

                for divisor in range(1, length):
                    if length % divisor != 0:
                        continue

                    group_size = length // divisor
                    changes = 0

                    for offset in range(divisor):
                        for t in range(group_size // 2):
                            a = left + offset + t * divisor
                            b = left + offset + (group_size - 1 - t) * divisor
                            if s[a] != s[b]:
                                changes += 1

                    cost[left][right] = min(cost[left][right], changes)
        
        #d[i][j] construction
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    dp[end][parts] = min(
                        dp[end][parts],
                        dp[start][parts - 1] + cost[start][end]
                    )

        return dp[n][k]

                


            