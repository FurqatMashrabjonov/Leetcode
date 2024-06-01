class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        found = -1
        for i in range(len(nums)):
            if nums[i] != i:
                found = i
                break
        
        if found == -1:
            found = len(nums)
            
        return found
        