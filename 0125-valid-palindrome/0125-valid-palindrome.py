class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanum = ''
        
        for char in s:
            if char.isalnum():
                alphanum += char
        
        
        l, r = 0, len(alphanum) - 1
        
        while l < r:
            if alphanum[l] != alphanum[r]:
                return False
            l += 1
            r -= 1
        
        return True