class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        row = len(grid)
        column = len(grid[0])
        def dfs(r, c):
            if r >= row or c >= column or r < 0 or c < 0 or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    island += 1
                    dfs(r,c)
        

        
        return island