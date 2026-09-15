class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        #dp[l][r] to get valid palindrome for each substring
        dp = [[False] * n for _ in range(n)]

        #palindrome calculation with dp
        for length in range(1, n+1):
            for left in range(0, n - length + 1, 1):
                right = left + length - 1
                if length <= 2:
                    dp[left][right] = s[left] == s[right]
                    continue

                if dp[left + 1][right - 1] and s[left] == s[right]:
                    dp[left][right] = True
        
        answer = 0
        start = 0
        for right in range(n):
            for length in (k, k + 1):

                left = right - length + 1

                if left >= start and dp[left][right]:
                    print(s[left:right+1])
                    answer += 1
                    start = right + 1
                    break
        return answer
                