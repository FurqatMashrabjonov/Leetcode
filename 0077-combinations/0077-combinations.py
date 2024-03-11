class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        
        def helper(i, curCombs, combs):
            if len(curCombs) >= k:
                combs.append(curCombs.copy())
                return None
            
            if i > n:
                return None
            
            curCombs.append(i)
            helper(i + 1, curCombs, combs)
            curCombs.pop()
            
            helper(i + 1, curCombs, combs)
            
            curCombs
        
        helper(1, [], combs)
        return combs