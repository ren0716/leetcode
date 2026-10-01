class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        #greedily close out open brackets asap to prevent nesting
        ans = [0] * len(seq)
        stack_a, stack_b = [], []
        for idx, char in enumerate(seq):
            if char == '(':
                if len(stack_a) > len(stack_b):
                    stack_b.append('(')
                    ans[idx] = 1
                else:
                    stack_a.append('(')
            else:
                if len(stack_a) > len(stack_b):
                    stack_a.pop()
                else:
                    stack_b.pop()
                    ans[idx] = 1
        return ans
