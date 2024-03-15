class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        
        def helper(i, comb, combs):
            cursum = sum(comb)
            if cursum == target:
                combs.append(comb.copy())
                return
            
            if cursum > target or i >= len(candidates):
                return
            
            comb.append(candidates[i])
            helper(i, comb, combs)
            comb.pop()
            
            helper(i + 1, comb, combs)
            
        helper(0, [], combs)
        
        return combs