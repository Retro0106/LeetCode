from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hashmap = {}
        # for char in strs:
        #     hashmap[char] = Counter(char)
        
        # res = []
        # my_set = set()

        # for i in range(len(strs)):
        #     if strs[i] not in my_set:
        #         curr = []
        #         my_set.add(strs[i])
        #         curr.append(strs[i])
                
        #         for j in range(len(strs)):
        #             if i != j and hashmap[strs[i]] == hashmap[strs[j]]:
        #                 curr.append(strs[j])
        #                 my_set.add(strs[j])
        #         res.append(list(curr))
        # return res

        # hashmap = {}
        # for char in strs:
        #     count = [0] * 26
        #     for letter in char:
        #         count[ord(letter)-ord('a')] += 1
        #     key = tuple(count)
        #     if key in hashmap:
        #         hashmap[key].append(char)
        #     else:
        #         hashmap[key] = [char]
        # return hashmap.values()
        hashmap = {}
        for char in strs:
            count = [0]*26
            for letter in char:
                count[ord(letter)-ord('a')] += 1
            key = tuple(count)
            hashmap[key] = hashmap.get(key, []) + [char]
        return hashmap.values()