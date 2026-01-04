class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def compute(num):
            curr = 0
            summ = 1 + num
            i = 2
            right = num
            while i < right:
                if num % i == 0:
                    curr += 1
                    right = num // i
                    if i == right:
                        return (0,-1)
                    summ += i + right
                i += 1
            return (summ, curr)
        total = 0
        for num in nums:
            current, number = compute(num)
            if number == 1:
                total += current
        return total