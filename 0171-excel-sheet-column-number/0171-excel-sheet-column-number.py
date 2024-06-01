class Solution:
    def getPositionNumber(self, c):
        return ord(c) - 64
    
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res += self.getPositionNumber(columnTitle[i]) * pow(26, len(columnTitle) - i - 1)
        
        return res