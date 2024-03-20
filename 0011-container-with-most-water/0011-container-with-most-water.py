class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        
        l, r = 0, len(height) - 1
        
        while l < r :
            hl, hr = height[l], height[r]
            s = (r - l) * min(hl, hr)
            
            m = max(s, m)
            
            if hl > hr:
                r -= 1
            else:
                l += 1
                
        return m