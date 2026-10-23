class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        carry = 1
        for pos, num in enumerate(nums):
            prefix[pos] = carry * num
            carry *= num

        prefix.insert(0, 1)
        
        carry = 1
        for pos in range(len(nums) - 1, -1, -1):
            suffix[pos] = carry * nums[pos]
            carry *= nums[pos]
        
        suffix.append(1)
        
        res = [0] * len(nums)
        for pos in range(len(nums)):
            res[pos] = prefix[pos] * suffix[pos + 1]
        
        return res
            
            

        