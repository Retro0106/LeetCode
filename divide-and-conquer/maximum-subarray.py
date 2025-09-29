class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maximum = float('-inf')

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maximum = max(curr, maximum)
        return maximum
            