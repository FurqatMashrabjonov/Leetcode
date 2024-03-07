class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        self.helper(0, candidates, [], combs, target)
        return combs
    
    
    
    def helper(self, i, nums, curCombs, combs, target):
        curSum = sum(curCombs)
        if curSum > target or i >= len(nums):
            return
        if curSum == target:
            combs.append(curCombs.copy())
            return
        
        curCombs.append(nums[i])
        self.helper(i, nums, curCombs, combs, target)
        curCombs.pop()
        
        self.helper(i + 1, nums, curCombs, combs, target)
        
        