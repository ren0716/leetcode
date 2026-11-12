class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        target = len(nums) // 2
        left, right = 0, len(nums) - 1

        # Quickselect: place the element that belongs at index target there.
        while left < right:
            pivot = nums[(left + right) // 2]

            # 3-way partition:
            # nums[left:lt] < pivot
            # nums[lt:i] == pivot
            # nums[i:gt + 1] unknown
            # nums[gt + 1:right + 1] > pivot
            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                break  # target falls among the values equal to pivot

        median = nums[target]
        return sum(abs(num - median) for num in nums)