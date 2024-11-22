class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lis = [i for i in s.split()]
        stringified = ''
        for i in lis[::-1]:
            stringified+=i+' '
        return stringified.strip()