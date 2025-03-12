class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[0] >= 0:
                return nums[i]
            elif nums[i] <= 0:
                continue
            if nums[i] >= 0 and nums[i-1] <= 0:
                return nums[i]
        return nums[-1]
    
        # hashmap = {}
        # for num in nums:
        #     key = abs(num)
        #     if key in hashmap:
        #         hashmap[key] = max(hashmap[key], num)
        #     else:
        #         hashmap[key] = num
        # return hashmap[min(hashmap.keys())]