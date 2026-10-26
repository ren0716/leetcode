class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #O(n3) bruteforce
        #hash all k -> largest pos
        #O(n2) scan of all i,j and check if 0 - k exist
        table = defaultdict(int, default=None)
        ans = []
        nums.sort()
        #initial populating of k table
        for idx, num in enumerate(nums):
            table[num] = idx
            
        #O(n2) double loop i,j scan
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j - 1 != i and nums[j] == nums[j - 1]:
                    continue
                req = 0 - nums[i] - nums[j]
                pos = table[req]
                if pos and pos > j:
                    ans.append([nums[i], nums[j], nums[pos]])
        
        return ans


        