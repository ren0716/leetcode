class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        #dp[i] longest consec subarray ending at index i
        #do i need to tabulate the ending number for the subarray?
        n = len(nums)
        nums.sort()
        dp = [[1, 1] for _ in range(n)]
        mx = 1
        for i in range(1, n):
            for j in range(0, 2):
                diff = nums[i] - nums[i - 1]
                if diff == 0:
                    dp[i][0] = dp[i - 1][0]
                    dp[i][1] = dp[i - 1][0] + 1
                elif diff == 1:
                    dp[i][0] = dp[i - 1][0] + 1
                    dp[i][1] = dp[i - 1][1] + 1
                elif diff == 2:
                    dp[i][0] = dp[i - 1][1] + 1
                    dp[i][1] = 1
                else:
                    continue
                mx = max(mx, dp[i][0], dp[i][1])

        return mx
                
            



        