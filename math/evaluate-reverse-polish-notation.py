class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def is_integer(s):
            try:
                int(s)
                return int(s)
            except ValueError:
                return False
        stack = []
        for i in tokens:
            if i.isdigit() or (i[0] == '-' and len(i) > 1):
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(int(a*b**-1))
        
        return stack[0]
                