class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        ans = float(abs(60*hour - 11*minutes))/2
        return ans if ans <= 180 else 360-ans