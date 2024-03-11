class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        
        def helper(i, curCombs, combs):
            sumVal = sum(curCombs)
            if sumVal == target:
                combs.append(curCombs.copy())
                return None
            
            if sumVal > target or i >= len(candidates):
                return None
            
            curCombs.append(candidates[i])
            helper(i, curCombs,combs)
            curCombs.pop()
            
            helper(i + 1, curCombs,combs)
            
            
        helper(0, [], combs)
        return combs