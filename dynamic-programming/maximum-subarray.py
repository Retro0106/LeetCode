class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        curr = 0
        for i in range(len(nums)):
            dp[i] = max(0, curr+nums[i])
            curr = dp[i]
        return max(dp)