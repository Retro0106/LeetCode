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

        for i in range(len(strs)):
            if strs[i] not in my_set:
                curr = set()
                my_set.add(strs[i])
                curr.add(strs[i])
                
                for j in range(len(strs)):
                    if i != j and hashmap[strs[i]] == hashmap[strs[j]]:
                        curr.add(strs[j])
                        my_set.add(strs[j])
                res.append(list(curr))
        return res

            