class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        self.p = 0
        
        def dfs(r, c):
            if (r, c) in visited:
                return
            
            if (
                min(r, c) < 0 or
                r >= ROWS or c >= COLS or grid[r][c] == 0
            ):
                self.p += 1
                return
            
            visited.add((r, c))
            
            for dr, dc in directs:
                dfs(r + dr, c + dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
        return self.p
                