class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #only increase not decrease -> benchmark on max val
        #find max
        mx = max(nums)
        acc = 0
        for num in nums:
            acc += (mx - num)
        return acc
        