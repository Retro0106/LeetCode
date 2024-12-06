from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return Counter(s) == Counter(t)

        # hashmap1 = {}
        # hashmap2 = {}
        # for i in s:
        #     hashmap1[i] = hashmap1.get(i, 0) + 1
        # for i in t:
        #     hashmap2[i] = hashmap2.get(i, 0) + 1
        # return hashmap1 == hashmap2

        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for i in t:
            if i not in hashmap:
                return False
            
            hashmap[i] -= 1
            if hashmap[i] == 0:
                del hashmap[i]
        return len(hashmap) == 0