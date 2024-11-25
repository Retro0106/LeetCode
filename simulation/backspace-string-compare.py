class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for char in s:
            if char == '#':
                stack1.pop()
            else:
                stack1.append(char)
        
        for char in t:
            if char == '#':
                stack2.pop()
            else:
                stack2.append(char)
        return stack1 == stack2