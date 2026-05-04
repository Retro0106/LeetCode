class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        index = left
        if index == 0:
            left = 0
            right = len(nums)-1

        elif nums[0] <= target <= nums[index-1]:
            left = 0
            right = index - 1
        
        else:
            left = index
            right = len(nums)-1

        while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1

