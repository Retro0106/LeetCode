import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = len(nums)
        heapq.heapify(nums)
        while count != k:
            heapq.heappop(nums)
            count -= 1
        return nums[0]
