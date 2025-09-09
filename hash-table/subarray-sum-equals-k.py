class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        curr = nums[left]
        count = 0

        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0

        while right < len(nums):
            while curr > k:
                curr -= nums[left]
                left += 1

            if curr == k:
                count += 1
                left += 1
                right += 1
            else:
                right += 1
                if right != len(nums):
                    curr += nums[right]


        return count