class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        visited = {}
        
        for c in s:
            if c not in visited:
                visited[c] = 1
                continue
                
            visited[c] += 1
        
        
        for c in t:
            if c not in visited:
                return False
            
            visited[c] -= 1
            
            if visited[c] < 0:
                return False
        
        
        return True