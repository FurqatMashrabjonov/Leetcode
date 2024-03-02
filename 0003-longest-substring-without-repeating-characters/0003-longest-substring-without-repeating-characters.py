class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxLen = 0
        l, r = 0, 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
        
            maxLen = max(maxLen, r - l + 1)
            window.add(s[r])    
            
        return maxLen