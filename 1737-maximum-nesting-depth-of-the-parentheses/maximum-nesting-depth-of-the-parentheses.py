class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        count = 0
        for char in s:
            if char == "(":
                count += 1

            if char == ")":
                count -= 1
            
            mx = max(mx, count)
        
        return mx
        