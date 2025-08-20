from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        hashmap = Counter(nums)
        bucket = [None] * len(nums)
        
        for key, value in hashmap.items():
            bucket[value] = key
        
        result = []
        count = 0
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                result.append(bucket[i])
                k -= 1
            if k == 0:
                return result
        
