
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()
        
        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = arr[left][0] + arr[right][0]
            
            if current_sum == target:
                return [arr[left][1], arr[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1