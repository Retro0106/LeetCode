class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = 'aeiou'
        maximum = 0
        left = 0
        right = k

        if len(s)==1:
            if s[0] in vowels:
                return 1
            return 0

        for i in s[:k]:
            if i in vowels:
                maximum += 1
        
        curr = maximum
        while right < len(s):
            if s[left] in vowels:
                curr -= 1
            if s[right] in vowels:
                curr += 1
            
            maximum = max(maximum, curr)
            left += 1
            right += 1
        return maximum

