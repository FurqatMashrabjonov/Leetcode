class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using hashMap
        obj = {}
        
        for i in range(len(nums)):
            if nums[i] in obj:
                return [obj[nums[i]], i]
            
            obj[target - nums[i]] = i