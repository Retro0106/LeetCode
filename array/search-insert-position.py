class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # initalize left, and right
        # while loop checking while left <= right
        # get mid
        # if mid is less, index = mid + 1, left = mid + 1
        # else, index = mid, right = mid - 1
        left, right = 0, len(nums)-1
        while left <= right: 
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                index  = mid + 1
                left = mid + 1
            if nums[mid] > target:
                index = mid
                right = mid - 1
        return index
                