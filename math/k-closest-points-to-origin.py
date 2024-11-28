import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(arr):
            return math.sqrt(arr[0]**2 + arr[1]**2)
        points.sort(key=distance)
        res = []
        for i in range(k):
            res.append(points[i])
        return res
