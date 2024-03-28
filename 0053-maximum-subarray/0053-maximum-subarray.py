class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        
        for num in nums:
            curSum = max(0, curSum)
            curSum += num
            maxSum = max(curSum, maxSum)
        
        return maxSum