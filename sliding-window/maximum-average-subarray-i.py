class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        if len(nums) <= 1:
            return nums[0]

        maximum = curr = sum(nums[:k])
        left = 0
        right = k


        while right < len(nums):
            curr -= nums[left]
            curr += nums[right]

            maximum = max(maximum, curr)
            left += 1
            right += 1
        return float(maximum)/k