class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # METHOD I
        result = 0
        for num in nums:
            result ^= num
        return result

        # METHOD II: O(n), o(n)
        # hashmap = {}
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1
        # for key in hashmap:
        #     if hashmap[key] == 1:
        #         return key

        # METHOD III: O(n^2), O(1)
        # for x in nums:
        #     if nums.count(x) == 1:
        #         return x