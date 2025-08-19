class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if 0 not in nums:
            return 0
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else: 
                return 0
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                return nums[i]+1
        return nums[i+1]+1
    