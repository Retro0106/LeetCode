class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        for i in range(x+1):
            if i * i > x:
                return i-1