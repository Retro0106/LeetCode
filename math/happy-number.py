class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        hashSet = set()
        def squareSum(num):
            res = 0
            for i in str(num):
                res += (int(i))**2
            return res

        while True:
            if n == 1:
                return True
            if n in hashSet:
                return False
            hashSet.add(n)
            n = squareSum(n)
        return False