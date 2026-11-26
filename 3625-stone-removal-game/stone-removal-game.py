class Solution:
    def canAliceWin(self, n: int) -> bool:
        #False -> alice turn
        turn = False
        remove = 10
        while n > 0 and remove <= n:
            n -= remove
            remove -= 1
            turn = not turn
        return turn
        