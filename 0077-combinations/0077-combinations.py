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
        
        curCombs.append(i)
        self.helper(i + 1, curCombs, combs, n, k)
        curCombs.pop()
        
        
        self.helper(i + 1, curCombs, combs, n, k)
        