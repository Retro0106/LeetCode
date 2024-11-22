from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

















        hashmap = defaultdict(int)
        highest = 0
        for i in nums:
            hashmap[i]+=1
            if hashmap[i] > len(nums)/2:
                return i
        
        for i in hashmap:
            if hashmap[i] > len(nums)/2:
                return i
            