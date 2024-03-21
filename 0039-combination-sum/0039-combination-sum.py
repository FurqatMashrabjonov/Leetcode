class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        
        def helper(i, comb, combs):
            curSum = sum(comb)
            if curSum == target:
                combs.append(comb.copy())
                return None
            
            if i >= len(candidates) or curSum > target:
                return None
            
            comb.append(candidates[i])
            helper(i, comb, combs)
            comb.pop()
            
            helper(i + 1, comb, combs)
            
        helper(0, [], combs)
        
        return combs
    