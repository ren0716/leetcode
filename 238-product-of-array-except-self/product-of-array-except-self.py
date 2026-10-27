class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #prefix/suffix i -> exclusive range in order to represent exclusion at boundaries
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        
        #build array
        carry = 1
        for idx, num in enumerate(nums):
            carry *= num
            prefix[idx + 1] = carry
        
        carry = 1
        for pos in range(len(nums) - 1, -1, -1):
            suffix[pos] = carry
            carry *= nums[pos]
        
        
        print(prefix)
        print(suffix)
        
        return [prefix[i] * suffix[i] for i in range(len(nums))]




        