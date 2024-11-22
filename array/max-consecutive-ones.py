class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        maximum = 0
        for i in nums:
            if i == 1:
                curr += 1
                maximum = max(maximum, curr)
            
            else:
                curr = 0
        return maximum
        
        # TC: O(n), SC: O(1)

        # if len(nums) == 1:
        #     if nums[0] == 1:
        #         return 1
        #     return 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] != 0:
        #         break
        #     i += 1
        # if i == len(nums):
        #     return 0
        # j = i+1
        # maximum = 0

        # while j < len(nums):
        #     if nums[j] == 0:
        #         maximum = max(maximum, j-i)
        #         i = j+1
        #         while i < len(nums):
        #             if nums[i] != 0:
        #                 break
        #             i+=1
        #         j = i+1
        #     else:
        #         j += 1
        
        # maximum = max(maximum, j-i)
        # return maximum