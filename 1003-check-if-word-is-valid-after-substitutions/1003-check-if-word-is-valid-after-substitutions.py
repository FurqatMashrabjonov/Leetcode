class Solution:
    def isValid(self, s: str) -> bool:
        d = "abc"
        i = 0
        while i < len(s):
            if s[i:i+3] == d:
                s = s[:i] + s[i + 3:]
                i = -1
            i+=1
        
        return len(s) == 0