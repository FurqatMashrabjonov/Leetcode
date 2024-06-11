class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        cur = prev = 1
        i = 2
        while i <= n:
            cur, prev = cur + prev, cur
            i += 1
        
        
        return cur