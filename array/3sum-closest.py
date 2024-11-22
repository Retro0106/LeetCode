class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hashmap = {}
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            complement = target - nums[i]
            while left < right:
                hashmap[(nums[i],nums[left],nums[right])]=abs(target-(nums[i]+nums[left]+nums[right]))
                closest = min(closest, abs(target - (nums[i]+nums[left]+nums[right])))
                if nums[left] + nums[right] < complement:
                    left += 1
                elif nums[left] + nums[right] > complement:
                    right -= 1
                else:
                    return target
        
        for num in hashmap:
            if hashmap[num] == closest:
                return sum(num)
        
        