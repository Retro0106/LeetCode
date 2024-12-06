class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # hashmap = {}
        # output = []
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1
        
        # rank = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        # for i in range(k):
        #     output.append(rank[i][0])
        # return output

        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        rank = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(rank[i][0])
        return output
