class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parents = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for c in s:
            if c in parents.keys():
                stack.append(parents[c])
            else:
                if len(stack) == 0:
                    return False
                
                cur = stack.pop()
                if cur != c:
                    return False
        
        return len(stack) == 0
