class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        #naive change all number to median
        nums.sort()
        median = nums[len(nums) // 2]
        acc = 0
        for num in nums:
            acc += abs(median - num)
        
        return acc

