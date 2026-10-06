class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # open and closing bracket must be the same
        stack = []
        for bracket in s:

            if bracket == '(':
                stack.append('(')

            if bracket == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
        return len(stack)

            
        