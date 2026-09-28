class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append("(")

            if char == ")":
                stack.pop()
            
            mx = max(mx, len(stack))
        
        return mx
        