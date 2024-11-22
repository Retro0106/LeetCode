from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashmap = Counter(arr)
        hash_set = set()
        for i in hashmap:
            if hashmap[i] in hash_set:
                return False
            hash_set.add(hashmap[i])
        return True