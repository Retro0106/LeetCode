from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        return all([True if hashmap[key]%2==0 else False for key in hashmap])
        