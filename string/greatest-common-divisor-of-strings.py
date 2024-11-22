class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        i = 0
        j = len(str2)-1
        while j >= 0:
            if len(str1)%len(str2[i:j+1]) == 0:
                if str2[i:j+1] * (len(str1)/len(str2[i:j+1])) == str1 and str2[i:j+1] * (len(str2)/len(str2[i:j+1])) == str2:
                    return str2[i:j+1]
            j-=1
        return ''
        






















        if str1 < str2:
            string = str1
        else:
            string = str2
        if string not in str1 or string not in str2:
            return ""
        n1 = len(str1) 
        n2 = len(str2)
        while string:
            if (n1 % len(string) != 0) or (n2 % len(string) != 0):
                string = string[0:-1]
            else:
                if string*(n1//len(string)) == str1 and string*(n2//len(string))==str2:
                    return string
                else:
                    string = string[0:-1]

        return ""
