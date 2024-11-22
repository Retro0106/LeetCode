from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = defaultdict(int)
        for mag in magazine:
            hashmap[mag] += 1
        
        for ran in ransomNote:
            hashmap[ran] -= 1
            if hashmap[ran] < 0:
                return False
        
        return True


























        # hashmap = {}
        # for mag in magazine:
        #     if mag in hashmap:
        #         hashmap[mag]+=1
        #     else:
        #         hashmap[mag] = 1
        # for ran in ransomNote:
        #     if ran not in hashmap:
        #         return False
        #     hashmap[ran]-=1
        #     if hashmap[ran] == 0:
        #         del hashmap[ran]
        # return True