class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        #hash row and col count
        rows = len(grid)
        cols = len(grid[0])
        row_tab = defaultdict(int)
        col_tab = defaultdict(int)
        #populate table O(nm)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    row_tab[row] += 1
                    col_tab[col] += 1
        #count servers
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row_tab[row] > 1 or col_tab[col] > 1):
                    count += 1

        return count
                    
    
        
