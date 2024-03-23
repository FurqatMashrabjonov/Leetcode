class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (
                min(r, c) < 0 or 
                r == ROWS or
                c == COLS or
                grid[r][c] == '0' or 
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        
        return islands