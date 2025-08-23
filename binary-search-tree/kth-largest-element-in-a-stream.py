import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = [-num for num in nums]
        self.nums = nums
        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int:
        lis = []
        lis.append(heapq.heappushpop(self.nums, -val))
        for i in range(self.k-2):
            lis.append(heapq.heappop(self.nums))

        answer = -self.nums[0]
        for num in lis:
            heapq.heappush(self.nums, num)
        return answer



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)