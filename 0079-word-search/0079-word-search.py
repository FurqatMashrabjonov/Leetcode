class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = []
        def helper(i, r, c):
            if i >= len(word):
                return
            
            if (
                min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in visited
            ):
                return
            
            if i == len(word) - 1:
                return True
            
            visited.append((r, c))
            
            res = (helper(i + 1, r, c + 1) or
                    helper(i + 1, r, c - 1) or
                    helper(i + 1, r + 1, c) or
                    helper(i + 1, r - 1, c))
            visited.remove((r, c))
            
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if helper(0, r, c):
                    return True
        return False