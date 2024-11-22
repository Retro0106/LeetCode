class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        maximum = 0
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            maximum = max(maximum, curr)
        return maximum