class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        import math

        def four_div_sum(n):
            total = 1 + n
            count = 2  # counting 1 and n

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    j = n // i
                    if i == j:          # perfect square → not valid
                        return 0
                    count += 2
                    total += i + j
                    if count > 4:       # early exit
                        return 0

            return total if count == 4 else 0

        return sum(four_div_sum(n) for n in nums)
