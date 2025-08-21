class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            digit = True
            try:
                int(token)
            except ValueError:
                digit = False
            if digit:
                stack.append(int(token))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[0]