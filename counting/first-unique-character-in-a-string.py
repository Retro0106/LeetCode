from collections import deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = deque()
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                q.append(s[i])
                hashmap[s[i]] = i
            else:
                if s[i] in q:
                    q.remove(s[i])
                
        if q:
            return hashmap[q[0]]
        return -1
            
        