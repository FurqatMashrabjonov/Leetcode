class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a_sum = int(((1 + n) * n) / 2)
        
        summa = 0
        for num in nums:
            summa += num
        
        
        
        return a_sum - summa
        
        