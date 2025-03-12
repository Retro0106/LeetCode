class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        def maximum(a, b):
            if abs(a) < abs(b):
                return a
            return b
    
        closest = nums[0]
        for num in nums:
            closest = maximum(closest, num)
        return closest
        # hashmap = {}
        # for num in nums:
        #     key = abs(num)
        #     if key in hashmap:
        #         hashmap[key] = max(hashmap[key], num)
        #     else:
        #         hashmap[key] = num
        # return hashmap[min(hashmap.keys())]