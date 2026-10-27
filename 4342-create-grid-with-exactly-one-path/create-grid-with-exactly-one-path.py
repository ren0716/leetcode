class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return [''.join(['.' if (i == n - 1 or j == 0) else '#' for i in range(n)]) for j in range(m)]
        