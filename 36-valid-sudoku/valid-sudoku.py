class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getGrid(r, c):
            return r // 3 * 3 + c // 3
        r_table = set()
        c_table = set()
        grid_table = set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]

                if char == ".":
                    continue

                if (row, char) in r_table:
                    return False
                else:
                    r_table.add((row, char))

                if (col, char) in c_table:
                    return False
                else:
                    c_table.add((col, char))
                
                grid = getGrid(row, col)
                if (grid, char) in grid_table:
                    return False
                else:
                    grid_table.add((grid, char))
        return True
        