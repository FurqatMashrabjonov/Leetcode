class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxS = 0
        while l < r:
            S = (r - l) * min(height[l], height[r])
            maxS = max(maxS, S)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxS