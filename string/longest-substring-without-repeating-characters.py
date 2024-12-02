class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashSet = set()
       
        if len(s) < 1:
            return 0
        longest = 1
        i = 0
        for j in range(len(s)):
            while s[j] in hashSet:
                longest = max(longest, j-i)
                hashSet.remove(s[i])
                i += 1
            hashSet.add(s[j])
        longest = max(longest, j-i+1)
        return longest