class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0: 
        #     return False
        # return str(x) == str(x)[::-1]
        num = x
        other = 0
        while x > 0:
            rem = x % 10
            x = x // 10
            other = other * 10 + rem
        
        return num == other