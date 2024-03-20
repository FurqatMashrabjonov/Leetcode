class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        
        for num in nums:
            if num in appeared:
                appeared[num] += 1
            else: 
                appeared[num] = 1
                
                
        for num in appeared.values():
            if num > 1:
                return True
            
        return False