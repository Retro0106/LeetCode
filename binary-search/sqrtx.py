class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # if x == 0:
        #     return 0

        # for i in range(x+1):
        #     if i * i > x:
        #         return i-1
        # return x

        if x == 0 or x== 1:
            return x
        half = x//2
        for i in range(half+1):
            if i * i > x:
                return i-1
            elif i*i == x:
                return i
        return x-1

