class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
          
        if target not in nums:
            return [-1,-1]
        else:
            left = nums.index(target)
            right = 0
            for i in range(len(nums)):
                if nums[i] == target:
                    right = i
        return [left, right]


            