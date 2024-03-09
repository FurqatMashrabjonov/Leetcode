class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token in operations:
                a = res.pop()
                b = res.pop()
                summ = 0
                if token == '+':
                    summ = a + b
                elif token == '-':
                    summ = b - a
                elif token == '/':
                    summ = int(b / a)
                else:
                    summ = a * b
                res.append(summ)
            else:
                res.append(int(token))
                
        return res[0]