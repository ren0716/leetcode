class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #check n - 1 and n + 1 of each element in the set -> worst case n^2?
        seen = set(nums)
        longest = 0
        for num in seen:
            curr = num
            count = 0
            if num - 1 not in seen:
                count += 1
                while curr + 1 in seen:
                    count += 1
                    curr += 1
            longest = max(count, longest)
        
        return longest 


        