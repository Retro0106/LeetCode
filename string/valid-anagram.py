from collections import Counter, defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_Counter = Counter(s)
        # t_Counter = Counter(t)
        # return s_Counter == t_Counter

        # hashmap = defaultdict(int)
        # for char in s:
        #     hashmap[char] += 1
        # for char in t:
        #     hashmap[char] -= 1
        #     if hashmap[char] == -1:
        #         return False
        # return max(hashmap.values()) == 0

        if len(s) != len(t):
            return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')]+=1
            count[ord(t[i]) - ord('a')]-=1
        return all(c==0 for c in count)