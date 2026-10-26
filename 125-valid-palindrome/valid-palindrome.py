class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2-pointer approach
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        right = len(s) - 1
        left = 0
        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        