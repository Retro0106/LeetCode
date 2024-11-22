class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1
        s = list(s)
        vowels = ('A','E','I','O','U','a','e','i','o','u')
        while i < j:
            while s[i] not in vowels and i < j:
                i+=1
            
            while s[j] not in vowels and i < j:
                j-=1
            
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return ''.join(s)






        # i = 0
        # j = len(s)-1
        # vowels = ['A','E','I','O','U','a','e','i','o','u']
        # lis = ['x']*len(s)
        # stringified = ''
        # if len(s)<2:
        #     return s
        # while i <= j:
        #     if s[i] in vowels and s[j] in vowels:
        #         lis[i]=s[j]
        #         lis[j]=s[i]
        #         i+=1
        #         j-=1
        #     elif s[i] in vowels:
        #         lis[j]=s[j]
        #         j-=1
        #     elif s[j] in vowels:
        #         lis[i]=s[i]
        #         i+=1
        #     else:
        #         lis[i]=s[i]
        #         lis[j]=s[j]
        #         i+=1
        #         j-=1
        
        # for i in lis:
        #     stringified+=i
        # return stringified
        

