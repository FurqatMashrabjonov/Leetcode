class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        
        maxLen = 1
        length = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] - nums[i - 1] == 1:
                length += 1
            else:
                length = 1
            
            maxLen = max(maxLen, length)
            
        return maxLen