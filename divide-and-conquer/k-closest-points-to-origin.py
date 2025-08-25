import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for point in points:
            distance = point[0]**2+point[1]**2
            if len(heap) == k:
                heapq.heappushpop(heap, [-distance, point])
            else:
                heapq.heappush(heap, [-distance, point])
        
        for each in heap:
            result.append(each[1])
        
        return result