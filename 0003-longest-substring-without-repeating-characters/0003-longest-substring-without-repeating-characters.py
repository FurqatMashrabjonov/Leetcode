class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l, r = 0, 0
        stack = set()
        for r in range(len(s)):
            while s[r] in stack:
                stack.remove(s[l])
                l += 1
            
            stack.add(s[r])
            maxLen = max(maxLen, r - l + 1)
                
        
        
        return maxLen