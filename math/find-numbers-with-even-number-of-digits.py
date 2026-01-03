class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def getNumber(num):
            count = 0
            while num > 0:
                num = num // 10
                count += 1
            return count

        total = 0
        for num in nums:
            if getNumber(num) % 2 == 0:
                total += 1
        return total