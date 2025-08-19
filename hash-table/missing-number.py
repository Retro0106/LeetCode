class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1
        for i in range(len(nums)):
            if i not in hashmap:
                return i
        return len(nums)