class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        obj = set()
        
        for num in nums:
            obj.add(num)
        
        for i in range(len(nums) + 1):
            if i not in obj:
                return i
        