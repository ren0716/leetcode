class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        #create prefix sum -> prefix[i] is exclusive of element i
        prefix = [0]
        acc = 0
        for num in nums:
            acc += num
            prefix.append(acc)
        
        mn = float('inf')
        for i in range(len(nums) + 1):
            for j in range(i, len(nums) + 1):
                if j - i < l or j - i > r:
                    continue
                sub_sum = prefix[j] - prefix[i]
                if sub_sum > 0:
                    mn = min(mn, sub_sum)

        return -1 if mn == float('inf') else mn        
            