class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = ''
        
        for c in s:
            if c.isalnum():
                a += c
        
        l, r = 0, len(a) - 1
        while l < r:
            if a[l] != a[r]:
                return False
            if a[l] == a[r]:
                l += 1
                r -= 1
            
        
        return True