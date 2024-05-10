class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        
        def helper(i, combs, comb):
            s = sum(comb)
            if s == target:
                combs.append(comb.copy())
                return None
            
            if i >= len(candidates) or s > target:
                return None
            
            comb.append(candidates[i])
            helper(i, combs, comb)
            comb.pop()
            
            helper(i + 1, combs, comb)
            
        
        helper(0, combs, [])
        
        return combs
            