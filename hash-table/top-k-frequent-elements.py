from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        bucket = [0] * (len(nums)+1)
        
        for key, value in hashmap.items():
            if bucket[value] == 0:
                bucket[value] = [key]
            else:
                bucket[value].append(key)
        
        result = []
        for i in range(len(nums),-1,-1):
            if bucket[i] != 0:
                result.extend(bucket[i])
                k-=len(bucket[i])
                if k == 0:
                    break
        return result