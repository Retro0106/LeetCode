class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        hashmap1 = {}
        hashmap2 = {}

        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hashmap1:
                if hashmap1[pattern[i]] != s[i] or hashmap2[s[i]] != pattern[i]:
                    return False
            if s[i] in hashmap2:
                if hashmap2[s[i]] != pattern[i]:
                    return False
            hashmap1[pattern[i]] = s[i]
            hashmap2[s[i]] = pattern[i]
        return True
            