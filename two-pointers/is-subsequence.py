class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) > len(t):
            return False
        for j in range(len(t)):
            if i == len(s):
                return True
            if t[j] == s[i]:
                i+=1
            
        return i == len(s)
