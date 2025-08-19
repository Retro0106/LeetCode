class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                if i - hashmap[nums[i]][-1] <= k:
                    return True
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]
        return False