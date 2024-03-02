class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        str = ''
        for char in s:
            if char.isalnum():
                str += char
        
        n = len(str)
        for i in range(n // 2):
            if str[i] != str[n - i - 1]:
                return False
        
        return True
                