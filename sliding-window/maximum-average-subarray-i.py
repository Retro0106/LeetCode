class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])

        curr = sum(nums[:k])
        maximum = float(curr / k)
        for i in range(len(nums)-k):
            curr -= nums[i]
            curr += nums[i+k]
            maximum = max(maximum, float(curr/k))
        return maximum

