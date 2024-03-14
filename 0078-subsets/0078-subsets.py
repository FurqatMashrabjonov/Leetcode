class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#         subsets = []
        
#         def helper(i, curSet, subsets):
#             if i >= len(nums):
#                 subsets.append(curSet.copy())
#                 return
#             curSet.append(nums[i])
#             helper(i + 1, curSet, subsets)
#             curSet.pop()

#             helper(i + 1, curSet, subsets)

#         helper(0, [], subsets)
        
#         return subsets


        subsets = []
        subsets.append([])
        for currentNumber in nums:
            n = len(subsets)
            for i in range(n):
                subsets.append(subsets[i] + [currentNumber])
        
        return subsets