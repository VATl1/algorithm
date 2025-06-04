class Solution(object):
    def evalRPN(self, tokens):
        stack = []
    
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                
                    result = int(a / b) if a * b >= 0 else -(-a // b)
                stack.append(result)
            else:
                stack.append(int(token))
    
        return stack[0]