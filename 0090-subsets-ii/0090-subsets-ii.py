class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        def helper(i, curSet, subsets):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return None
        
            
            curSet.append(nums[i])
            helper(i + 1, curSet, subsets)
            curSet.pop()
            
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            helper(i + 1, curSet, subsets)
            
        helper(0, [], subsets)
        
        return subsets