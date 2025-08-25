import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            if a != b:
                heapq.heappush(heap, a-b)
        
        if len(heap) == 1:
            return -heap[0]
        else:
            return 0
        

