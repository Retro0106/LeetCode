class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
         
        i = j = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                j = i+1
                while j < len(nums):
                    if nums[j] != 0:
                        nums[i],nums[j] = nums[j], nums[i]
                        break
                    j += 1
            i += 1
        


        