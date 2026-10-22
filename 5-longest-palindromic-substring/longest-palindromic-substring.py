class Solution:
    def longestPalindrome(self, s: str) -> str:
        #O(n^2) dp problem that iterates start and end point
        #individual letters on the dp table first
        #cases -> len == 1, len == 2 
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        longest = ''
        #traverse order left -> right, up -> down
        for start in range(len(s), -1, -1):
            for end in range(start, len(s), 1):
                if start == end:
                    dp[start][end] = True
                elif end - start == 1:
                    dp[start][end] = (s[start] == s[end])
                else:
                    dp[start][end] = dp[start + 1][end - 1] and (s[start] == s[end])

                if dp[start][end]:
                    longest = longest if len(longest) >= (end - start + 1) else s[start: end + 1]

        return longest


            
        
        