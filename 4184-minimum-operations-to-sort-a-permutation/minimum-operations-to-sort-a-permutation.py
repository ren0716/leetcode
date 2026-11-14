class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        pos = nums.index(0)

        # Read forward from 0: 0, 1, 2, ..., n-1
        forward = all(nums[(pos + i) % n] == i for i in range(n))

        # Read backward from 0: 0, 1, 2, ..., n-1
        backward = all(nums[(pos - i) % n] == i for i in range(n))

        ans = float("inf")

        if forward:
            # Rotate left pos times.
            # Or use two reversals to get the equivalent opposite rotation.
            ans = min(ans, pos, n - pos + 2)

        if backward:
            # After reversing, 0 is at reversed_pos.
            reversed_pos = n - 1 - pos
            # Reverse, then rotate; or rotate the other way, then reverse.
            ans = min(ans, 1 + min(reversed_pos, n - reversed_pos))

        return -1 if ans == float("inf") else ans