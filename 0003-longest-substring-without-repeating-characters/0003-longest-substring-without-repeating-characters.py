class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        sub = set()
        l, r = 0, 0
        
        while r < len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            
            sub.add(s[r])
            
            maxLen = max(maxLen, len(sub))
            r += 1
            
        return maxLen