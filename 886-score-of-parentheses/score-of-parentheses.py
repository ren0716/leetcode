class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # o(n) scan to find matching brackets first
        self.matched = [-1] * len(s)
        stack = []
        for idx, bracket in enumerate(s):
            if bracket == '(':
                stack.append(idx)
            else:
                openpos = stack.pop()
                self.matched[idx] = openpos
                self.matched[openpos] = idx
        
        # score function
        def scorer(mult, start, end):
            if end - start == 1:
                return mult * 1
            else:
                if self.matched[start] == end:
                    return scorer(mult * 2, start + 1, end - 1)
                else:
                    mid = self.matched[start]
                    return scorer(mult, start, mid) + scorer(mult, mid + 1, end)
                    
        return scorer(1, 0, len(s) - 1)
        



            
        