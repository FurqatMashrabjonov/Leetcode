class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        hashMap = {}
        while r < len(nums):
            if r - l > k:
                del hashMap[nums[l]]
                l += 1
            
            if nums[r] in hashMap:
                return True
            
            hashMap[nums[r]] = 1
            r += 1
        return False