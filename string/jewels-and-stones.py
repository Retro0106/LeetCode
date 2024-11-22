class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        a = set(jewels)
        count = 0
        for i in stones:
            if i in a:
                count+=1
        return count
