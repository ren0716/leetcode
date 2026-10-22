class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        flow_p = [[False] * cols for _ in range(rows)]
        flow_a = [[False] * cols for _ in range(rows)]

        def dfs(r, c, reached):
            reached[r][c] = True

            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not reached[nr][nc]
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, reached)

        for c in range(cols):
            dfs(0, c, flow_p)           # top edge
            dfs(rows - 1, c, flow_a)    # bottom edge

        for r in range(rows):
            dfs(r, 0, flow_p)           # left edge
            dfs(r, cols - 1, flow_a)    # right edge

        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if flow_p[r][c] and flow_a[r][c]
        ]