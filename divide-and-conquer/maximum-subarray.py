class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')]*len(nums)
        array = [float('-inf')]*len(nums)

        array[0] = nums[0]
        
        curr = max(0, nums[0])
        for i in range(1, len(nums)):
            dp[i] = max(0, curr+nums[i])
            curr = dp[i]
            array[i] = max(array[i-1], curr)
            
        return max(array)