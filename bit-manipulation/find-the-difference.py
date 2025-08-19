from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap2 = Counter(s)
        for i in range(len(t)):
            if t[i] in hashmap2:
                if hashmap2[t[i]] == 0:
                    return t[i]
                hashmap2[t[i]] -= 1
            else:
                return t[i]