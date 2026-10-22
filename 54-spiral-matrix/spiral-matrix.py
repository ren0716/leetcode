class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []

        while left <= right and top <= bottom:
            # Traverse right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Traverse down
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # Traverse left, if a row remains
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Traverse up, if a column remains
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res