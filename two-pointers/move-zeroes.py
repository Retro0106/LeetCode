class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

            
        

        
        # Doesnt keep the order intact

        # i = 0
        # j = len(nums)-1
        # while nums[j] == 0 and j>=0:
        #     j-=1
        # while i < j:
        #     if nums[i] == 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #     i+=1