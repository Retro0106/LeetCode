class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # TEST 1

        # if x == 0:
        #     return 0

        # for i in range(x+1):
        #     if i * i > x:
        #         return i-1
        # return x

        
        
        
        
        # TEST 2

        # if x == 0 or x== 1:
        #     return x
        # half = x//2
        # for i in range(half+2):
        #     if i * i > x:
        #         return i-1
        #     elif i*i == x:
        #         return i
        # return x-1

        if x == 0 or x== 1:
            return x
        right = x
        left = 0
        mid = (left + right) // 2
        temp = False

        while left < right:
            mid = (left + right) // 2

            if temp and mid == temp:
                if (mid+1) * (mid+1) > x:
                    return mid 
                return mid + 1
            
            if mid * mid == x:
                return mid
            
            elif mid * mid < x:
                left = mid
            
            elif mid * mid > x:
                right = mid - 1 
            
            temp = mid
        return left
            


