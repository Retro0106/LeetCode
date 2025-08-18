class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # j = len(nums)-1
        # while nums[j] == 0 and j > 0:
        #     j-=1
        # if j <= 0:
        #     return nums
        # while i < j:
        #     if nums[i] == 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #     i += 1
        # return nums
        i = 0
        while nums[i] != 0 and i < len(nums):
            i += 1
        if i == len(nums):
            return nums
        
        for j in range(i, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums