class Solution:
    def checkString(self, s: str) -> bool:
        b_seen = False
        for char in s:
            if char == 'b':
                b_seen = True
            if b_seen and char == 'a':
                return False
        return True
        