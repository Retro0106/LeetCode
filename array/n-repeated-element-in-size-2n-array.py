from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for num in hashmap:
            if hashmap[num] == len(nums)//2:
                return num