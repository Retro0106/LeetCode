class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'[':']','{':'}','(':')'}

        for char in s:
            if char not in hashmap:
                if stack:
                    curr = stack.pop()
                    if hashmap[curr] != char:
                        return False
            else:
                stack.append(char)
        return len(stack) == 0