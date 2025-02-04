class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
          
        # if target not in nums:
        #     return [-1,-1]
        # else:
        #     left = nums.index(target)
        #     right = 0
        #     for i in range(len(nums)):
        #         if nums[i] == target:
        #             right = i
        # return [left, right]

        if target not in nums:
            return [-1, -1]
         
        def searchLeft(nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid
                    if right != 0 and nums[right - 1] != target:
                        return right
                elif mid < target:
                    left = mid + 1
                elif mid > target:
                    right = mid - 1
            


        def searchRight(nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left = mid
                    if left != 0 and nums[left + 1] != target:
                        return left
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
        return [searchLeft(nums), searchRight(nums)]

