class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l_array = [1 for i in nums]
        r_array = [1 for i in nums]
        l_multiplier = r_multiplier = 1
        i = 0
        j = len(nums)-1
        while i < len(nums):
            l_array[i]=l_multiplier
            r_array[j]=r_multiplier
            l_multiplier*=nums[i]
            r_multiplier*=nums[j]
            i+=1
            j-=1
        answer = list(map(lambda x,y:x*y,l_array,r_array))
        return answer
        
        
        
        
        
        
        
        
        
        
        
        # answer = [] 
        # i = j = 0 
        # mult = 1
        # mult_with_zero = 1   
        # for i in nums:
        #     if i!= 0:
        #         mult*=i
        #     mult_with_zero *=i
        # for i in nums:
        #     if i!= 0:
        #         if 0 in nums:
        #             answer.append(0)
        #         else:
        #             answer.append(mult//i)
        #     else:
        #         if max(nums)==0:
        #             answer.append(0)
        #         elif nums.count(i)>1:
        #             answer.append(mult_with_zero)
        #         else:
        #             answer.append(mult)
        # return answer







        # while i < len(nums) and j < len(nums):
        #     if j == len(nums) -1:
        #         if i != j:
        #             mult*=nums[j]
        #         j=0
        #         i+=1
        #         answer.append(mult)
        #         mult = 1
        #     else:
        #         if i != j:
        #             mult*=nums[j]
        #         j+=1     
        # return answer
                