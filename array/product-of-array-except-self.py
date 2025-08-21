class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        lmult = 1
        rmult = 1

        for i in range(len(nums)):
            left[i] = lmult
            lmult *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            right[i] = rmult
            rmult *= nums[i]
        
        return list(map(lambda x,y: x*y, left, right))
