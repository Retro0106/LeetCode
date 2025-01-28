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

        # while left < right:
        #     mid = (left + right) // 2

        #     if temp and mid == temp:
        #         if (mid+1) * (mid+1) > x:
        #             return mid 
        #         return mid + 1
            
        #     if mid * mid == x:
        #         return mid
            
        #     elif mid * mid < x:
        #         left = mid
            
        #     elif mid * mid > x:
        #         right = mid - 1 
            
        #     temp = mid
        # return left
            

        if x < 2:  # Special case for 0 and 1
            return x

        left, right = 1, x // 2  # Binary search range: from 1 to x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:  # Exact square root found
                return mid
            elif mid * mid < x:  # Move right if mid^2 is less than x
                left = mid + 1
            else:  # Move left if mid^2 is greater than x
                right = mid - 1

        # At this point, `right` is the largest integer such that `right^2 <= x`
        return right


