class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')]*len(nums)

        dp[0] = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, curr+nums[i])
            curr = dp[i]
        return max(dp)