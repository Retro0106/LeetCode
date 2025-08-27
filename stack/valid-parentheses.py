class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'(':')', '{':'}', '[':']'}

        for char in s:
            if char not in hashmap:
                if stack:
                    a = stack.pop()
                    if hashmap[a] != char:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return not stack