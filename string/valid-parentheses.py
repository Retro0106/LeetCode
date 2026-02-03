class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(':')','[':']','{':'}'}

        stack = []
        for char in s:
            if not stack:
                if char not in hashmap:
                    return False
                stack.append(char)
            else:
                if char not in hashmap:
                    if hashmap[stack[-1]] != char:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(char)
        return len(stack)==0
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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