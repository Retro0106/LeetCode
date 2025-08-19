class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            if i == len(nums):
                return count
            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1
            count += ((j- i)*(j-i+1)//2)
            if j == len(nums):
                return count
            i = j
        return count
            
            