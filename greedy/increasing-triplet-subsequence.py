class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) < 3:
            return False
        left_min = float('inf')
        right_max = 0
        left_array = [0]*len(nums)

        
        right_array = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1] > right_max:
                right_max = nums[i+1]
            right_array[i] = right_max
         

        for i in range(1,len(nums)-1):
            if nums[i-1] < left_min:
                left_min = nums[i-1]
            left_array[i] = left_min
            
            if left_array[i] < nums[i] and nums[i] < right_array[i]:
                return True

        return False
        
