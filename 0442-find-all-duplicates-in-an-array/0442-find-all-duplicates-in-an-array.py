class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_set = set()
        res = []
        for num in nums:
            if num in hash_set:
                res.append(num)
            
            hash_set.add(num)
        
        return res