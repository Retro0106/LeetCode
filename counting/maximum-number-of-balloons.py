from collections import defaultdict
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        hashmap = defaultdict(int)
        
        for i in text:
            if i in 'balon':
                hashmap[i] += 1
        
        for i in 'balon':
            if i not in hashmap:
                return 0
        
        if hashmap['l'] < 2 or hashmap['o'] < 2:
            return 0
        
        
        hashmap['l'] = hashmap['l']//2
        hashmap['o'] = hashmap['o']//2

        return min(hashmap.values())
        
