class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        
        left = 0  
        right = len(nums) - 1  

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1  
            else:
                left += 1  
        return left

        
        
        
        # i = 0
        # j = len(nums)-1
        # if len(nums)==1 and nums[i]==val:
        #     return i
        # while i < j:
        #     while nums[j] == val and j >= 0:
        #         j -= 1
        #     if j < 0:
        #         return i
        #     if nums[i] == val:
        #         nums[i],nums[j] = nums[j], nums[i]
        #         j-=1
        #     i+=1
            
        # return i+1

















        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[index] = nums[i]
        #         index += 1
        # return index
       
       
       
       
        # count = 0
        # i = 0
        # n = len(nums)

        # while i < n:
        #     if nums[i] == val:
        #         nums.pop(i)
        #         n-=1
                
        #     else:
        #         count+=1
        #         i+=1
        # return count
                