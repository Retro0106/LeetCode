class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap1 = {}
        hashmap2 = {}
        for i in range(len(s)):
            if s[i] in hashmap1:
                if hashmap1[s[i]] != t[i]:
                    return False
            
            hashmap1[s[i]] = t[i]
            if t[i] in hashmap2:
                if hashmap2[t[i]] != s[i]:
                    return False
            hashmap2[hashmap1[s[i]]] = s[i]
        return True
        
        
        
        # hashmap = {}
        # for i in range(len(s)):
        #     if s[i] in hashmap:
        #         if hashmap[s[i]] != t[i]:
        #             return False
        #     for a in hashmap:
        #         if hashmap[a] == t[i] and s[i] != a:
        #             return False
        #     hashmap[s[i]] = t[i]
        # return True
