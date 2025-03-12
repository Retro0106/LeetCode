class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            key = abs(num)
            if key in hashmap:
                hashmap[key] = max(hashmap[key], num)
            else:
                hashmap[key] = num
        return hashmap[min(hashmap.keys())]