class Solution:
    
    def titleToNumber(self, col: str) -> int:
        res = 0
        for i in range(len(col)):
            res += (ord(col[i]) - 64) * pow(26, len(col) - i - 1)
        
        return res