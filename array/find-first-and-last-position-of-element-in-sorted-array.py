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

        
         
        if not nums:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        elif len(nums) == 2:
            if nums[0] == target and nums[1] == target:
                return [0,1]
            elif nums[0] == target:
                return [0,0]
            elif nums[1] == target:
                return [1,1]
            else:
                return [-1,-1]
        def searchLeft(nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid
                    if (right != 0 and nums[right - 1] != target) or right == 0:
                        return right
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                
            return right if nums[right] == target else -1
            


        def searchRight(nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left = mid
                    if (left != len(nums)-1 and nums[left + 1] != target) or left == len(nums) -1:
                        return left
                    elif left != len(nums)-1 and nums[left + 1] == target:
                        left += 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                
            return left if nums[left] == target else -1
        return [searchLeft(nums), searchRight(nums)]