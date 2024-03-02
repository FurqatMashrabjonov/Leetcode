class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        exists = {}
        l = 0
        for r in range(len(nums)):
            
            if abs(l - r) > k:
                del exists[nums[l]]
                l += 1
                
            if nums[r] in exists:
                return True
            
            exists[nums[r]] = True
            
        return False