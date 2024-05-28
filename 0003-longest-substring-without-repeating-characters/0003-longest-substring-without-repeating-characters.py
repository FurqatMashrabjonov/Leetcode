class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        sub = ''
        l, r = 0, 0
        while r < len(s):
            while s[r] in sub:
                sub = sub[1:]
                l += 1
                
            sub = s[l:r + 1]
            max_ = max(max_, len(sub))
            
            r += 1
        
        
        return max_