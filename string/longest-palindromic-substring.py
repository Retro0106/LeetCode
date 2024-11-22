class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len(s)<=1:
        #     return s
        # max_len = 0
        # max_str = s[0]
        # for i in range(len(s)-1):
        #     for j in range(i+1,len(s)):
        #         if j-i+1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
        #             max_len = j-i+1
        #             max_str = s[i:j+1]
        # return max_str

        def expand(left, right):
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        max_str = s[0]
        for i in range(len(s)-1):
            odd = expand(i,i)
            even = expand(i,i+1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        return max_str
