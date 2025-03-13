class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
        
        output = []
        hset = set(nums2)
        for num in set(nums1):
            if num in hset:
                output.append(num)
        return output