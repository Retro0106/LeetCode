class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                if summ == k:
                    count += 1
        return count