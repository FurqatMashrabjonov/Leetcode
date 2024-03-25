class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        def helper(i, comb):
            curSum = sum(comb)
            if curSum == target:
                combs.append(comb.copy())
                return
            
            
            if i >= len(candidates) or curSum > target:
                return
            
            comb.append(candidates[i])
            helper(i + 1, comb)
            comb.pop()
            
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                
            helper(i + 1, comb)
        helper(0, [])
        return combs