class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        obj = {}
        
        for num in nums:
            obj[num] = 1 + obj.get(num, 0)
        
        for item in obj:
            if obj[item] != 2:
                return item