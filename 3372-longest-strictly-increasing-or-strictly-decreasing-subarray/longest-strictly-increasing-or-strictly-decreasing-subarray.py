class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        #Boolean switch with none to indicate unknown pattern
        #longest tracker
        isIncreasing = None
        longest = 1
        curr = 1
        for i in range(1, len(nums)):

            if isIncreasing is None:
                isIncreasing = nums[i] > nums[i - 1]

            if isIncreasing and nums[i] > nums[i - 1]:
                curr += 1
            
            elif not isIncreasing and nums[i] < nums[i - 1]:
                curr += 1
            
            else:
                isIncreasing = None if nums[i] == nums[i - 1] else nums[i] > nums[i - 1]
                curr = 1 if nums[i] == nums[i - 1] else 2
                
            
            longest = max(curr, longest)
        
        return longest

        