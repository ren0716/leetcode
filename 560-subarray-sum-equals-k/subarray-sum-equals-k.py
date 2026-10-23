class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #O(n^2) solution is to use prefix array and check every ij combination
        count = 0
        prefix = [0] * len(nums)
        carry = 0
        #each pos is the prefix sum including self
        for pos, num in enumerate(nums):
            carry += num
            prefix[pos] = carry
        
        #optimise by using set() to check for existence -> use dict to track freq as well
        seen = defaultdict(int)
        seen[0] = 1
        for val in prefix:
            #find target val
            target = val - k

            #check seen and freq
            if target in seen:
                count += seen[target]
                
            #update freq
            seen[val] += 1
        
        return count


            

        