class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """

        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1


























        # i = 1
        # for j in range(1,len(nums)):
        #     if nums[j] != nums[i-1]:
        #         nums[i] = nums[j]
        #         i+=1
        # return i


        
        
        
        
        
        # i = 0
        # other = sorted(list(set(nums)))
        # while i < len(other):
        #     j = i
        #     if nums[i] == other[j]:
        #         i+=1
        #     else:
        #         nums.pop(i)
        # return len(other)



        # for i in range(len(nums)-1):
        #     j = i+1
        #     while j < len(nums):
        #         if nums[j] != nums[i] and nums[i]<=nums[j]:
        #             nums[i+1],nums[j] = nums[j],nums[i+1]
        #             break
        #         j+=1
        # return len(set(nums))







        # another = set(nums)
        # redo = list(another)
        # redo.sort()
        # result = len(redo)
        # for num in redo[::-1]:
        #     nums.insert(0,num)
        # return result
        
            