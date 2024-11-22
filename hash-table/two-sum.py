class Solution(object):
    def twoSum(self, nums, target):
       
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num] = i
            

        

       
       
       
       
        # i = 0
        # lis = [] 
        # while i < len(nums):
        #     a = (target - nums[i])
        #     if a in nums and nums.index(a) != i:
        #         lis.append(i)
        #         lis.append(nums.index(a))
        #         return lis
        #     i+=1
        