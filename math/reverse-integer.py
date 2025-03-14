class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
        integer = abs(x)
        reverse = 0
        while integer > 0:
            curr = integer % 10
            integer = round(integer // 10)
            reverse = reverse * 10 + curr
        
        return -reverse if negative else reverse
