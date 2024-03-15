class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        def helper(i, comb, combs):
            curSum = sum(comb)
            if curSum == target:
                combs.append(comb.copy())
                return
            
            
            if curSum > target or i >= len(candidates):
                return
            
            comb.append(candidates[i])
            helper(i + 1, comb, combs)
            comb.pop()
            
            
            while i + 1< len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                
            helper(i + 1, comb, combs)
            
        helper(0, [], combs)
        
        return combs