from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for char in strs:
            hashmap[char] = Counter(char)
        
        res = []
        my_set = set()

        for char in hashmap:
            if char not in my_set:
                curr = set()
                my_set.add(char)
                curr.add(char)
                
                for j in hashmap:
                    if hashmap[char] == hashmap[j]:
                        curr.add(j)
                        my_set.add(j)
                res.append(list(curr))
        return res

            