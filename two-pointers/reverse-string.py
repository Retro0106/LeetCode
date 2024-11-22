class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        other = s
        while left<=right:
            left_char = s[left]
            right_char = s[right]
            
            s[left] = right_char
            s[right] = left_char
            left+=1
            right-=1
            
        

            

        