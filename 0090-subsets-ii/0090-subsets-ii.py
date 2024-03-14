class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        
        def helper(i, nums, cur, subsets):
            if i >= len(nums):
                subsets.append(cur.copy())
                return
            
            cur.append(nums[i])
            helper(i + 1, nums, cur, subsets)
            cur.pop()
            
        
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
        
            helper(i + 1, nums, cur, subsets)
        
        helper(0, nums, [], subsets)
        
        return subsets