class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        
        for num in nums:
            if num in appeared:
                appeared[num] += 1
            else: 
                appeared[num] = 1
            
            if appeared[num]  > 1:
                return True
                
                
        return False