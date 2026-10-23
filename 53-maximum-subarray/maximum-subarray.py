class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #simple dp to determine if reset
        #max of sum of nums ending at i
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
        #traverse and find largest dp[i]
        largest = float('-inf')
        for val in dp:
            largest = max(val, largest)
        
        return largest
        