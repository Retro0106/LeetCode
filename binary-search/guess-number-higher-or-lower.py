# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = (left+right) // 2
        while left < right:
            my_guess = guess(mid)
            if my_guess == 1:
                left = mid + 1
            elif my_guess == -1:
                right = mid
            else:
                return mid
            mid = (left+right) // 2
        return mid
            