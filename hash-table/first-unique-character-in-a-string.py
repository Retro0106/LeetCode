from collections import deque, Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # q = deque()
        # hashmap = {}
        
        # for i in range(len(s)):
        #     if s[i] not in hashmap:
        #         q.append(s[i])
        #         hashmap[s[i]] = i
        #     else:
        #         if s[i] in q:
        #             q.remove(s[i])
                
        # return hashmap[q[0]] if q else -1
            
        freq = Counter(s)
        for i, j in enumerate(s):
            if freq[j] == 1:
                return i
        return -1