class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVal = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            S = (r - l) * min(height[l], height[r])
            
            maxVal = max(maxVal, S)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
        return maxVal