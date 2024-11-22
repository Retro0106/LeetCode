class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        set_res = set()

        for k in range(len(nums)-2):
            target = -nums[k]
            if nums[k] == nums[k-1] and k > 0:
                continue
            i = k+1
            j = len(nums)-1
            while i < j:
                if nums[i] + nums[j] == target:
                    if (nums[k],nums[i],nums[j]) not in set_res:
                        res.append([nums[k],nums[i],nums[j]])
                        set_res.add((nums[k],nums[i],nums[j]))
                    i += 1
                elif nums[i] + nums[j] <= target:
                    i+=1
                else:
                    j-=1
        return res













        # output = set()
        
        # nums.sort()
        # for curr in range(0,len(nums)-2):
        #     i = curr + 1
        #     j = len(nums)-1
        #     while i < j:
        #         if nums[curr] + nums[i] + nums[j] == 0:
        #             output.add((nums[curr],nums[i],nums[j]))
        #         elif nums[curr] + nums[i] + nums[j] <= 0:
        #             i += 1
        #         else:
        #             j-=1
        # output = list(output)
        


        return output


        # for i in range(len(nums)-2):
        #     left = i+1
        #     right = len(nums)-1
        #     while left < right:
        #         if nums[left] + nums[right] == hashmap[nums[i]]:
        #             output.append([nums[i],nums[left],nums[right]])
        #             break
        #         elif nums[left] + nums[right] < hashmap[nums[i]]:
        #             left+=1
        #         else:
        #             right-=1
        # for row in output:
        #     row = tuple(row)
        #     result.append(row)
        # return output





        # output = []
        # for i in nums:
        #     for j in range(1,len(nums)):
        #         for k in range(2,len(nums)):
        #             if  nums[i]+nums[j]+nums[k]== 0:
        #                 output+[i,j,k]
        # return output

