class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        self.helper(0, nums, subsets, curSet)
        return subsets
    
    
    def helper(self, i, nums, subsets, curSet):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return
        #include nums[i]
        curSet.append(nums[i])
        self.helper(i + 1, nums, subsets, curSet)
        curSet.pop()
        #not include nums[i]
        self.helper(i + 1, nums, subsets,curSet)