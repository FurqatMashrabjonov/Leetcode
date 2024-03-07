class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs
    
    def helper(self, i, curCombs, combs, n, k):
        if len(curCombs) == k:
            combs.append(curCombs.copy())
            return 
        
        if i > n:
            return
        
        for j in range(i, n + 1):
            curCombs.append(j)
            self.helper(j + 1, curCombs, combs, n, k)
            curCombs.pop()