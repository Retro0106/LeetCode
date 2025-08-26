import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        power = int(math.log(n,3))
        return n == 3**power