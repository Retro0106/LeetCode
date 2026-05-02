class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initiaize left as 0, right as len(nums)-1
        # while left < right:
        # get mid index and check if its equal to target
        # if its less left = mid + 1
        # if its greater right = mid - 1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return -1