class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        hashSet = set()

        left = 0

        longest = 0
        for right in range(len(s)):
            if s[right] in hashSet:
                longest = max(longest, right - left)
                while s[left] != s[right]:
                    left += 1
                
                left += 1
            
            hashSet.add(s[right])
        longest = max(longest, right - left)
        return longest