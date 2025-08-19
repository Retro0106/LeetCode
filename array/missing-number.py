class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = 1
        # for i in range(len(nums)):
        #     if i not in hashmap:
        #         return i
        # return len(nums)
        n = len(nums)
        total = (n+1)*n//2
        for num in nums:
            total -= num
        return total