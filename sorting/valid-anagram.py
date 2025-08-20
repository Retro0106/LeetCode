from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = Counter(s)
        hashmap2 = Counter(t)
        return hashmap == hashmap2