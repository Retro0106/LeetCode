class Solution(object):
    def isValid(self, s):
        count = 0
        hashmap = {'(':')', '{':'}', '[':']'}
        
        def is_open(string):
            return string in hashmap
        array = []

        for i in s:
            if is_open(i):
                array.append(i)
            else: 
                if not array:
                    return False
                removed = array.pop()
                if hashmap[removed] != i:
                    return False
        return not array
        
        