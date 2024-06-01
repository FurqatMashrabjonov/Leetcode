class Solution:
    def getPos(self, c):
        return ord(c) - 64
    
    def titleToNumber(self, col: str) -> int:
        res = 0
        for i in range(len(col)):
            res += self.getPos(col[i]) * pow(26, len(col) - i - 1)
        
        return res