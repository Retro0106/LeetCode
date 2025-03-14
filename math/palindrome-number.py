class Solution:
    def isPalindrome(self, x: int) -> bool:
        # string = str(x)
        # return string == string[::-1]
        if x < 0:
            return False
        integer = x
        backwards = 0
        while integer > 0:
            curr = integer % 10
            integer = round(integer // 10)
            backwards = backwards * 10 + curr
        return backwards == x
            