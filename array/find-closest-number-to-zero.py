class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = nums[0]
        for i in nums:
            if abs(i) < abs(smallest):
                smallest = i
            elif abs(i) == abs(smallest):
                smallest = max(i, smallest)
        return smallest