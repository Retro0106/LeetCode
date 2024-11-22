class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
                max_length = max(max_length, current_length)                
        return max_length



        # BRUTE FORCE APPROACH O(nlogn)

        # if not nums:
        #     return 0
        # max_length = 0
        # i = 0
        # j = 1
        # nums = list(set(nums))
        # nums.sort()
        # while j < len(nums):
        #     if nums[j] != nums[j-1] + 1:
        #         max_length = max(max_length, j-i)
        #         i = j
        #     j += 1
        
        # max_length = max(max_length, j-i)
        # return max_length