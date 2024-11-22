class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []

        num1 = [i for i in nums1 if i not in nums2]
        num2 = [i for i in nums2 if i not in nums1]
        result.append(num1)
        result.append(num2)
        return result
        
        # USING SET METHODS - TC: O(n+m), SC: O(n+m)

        # result = []
        # result.append(list(set(nums1).difference(set(nums2))))
        # result.append(list(set(nums2).difference(set(nums1))))
        # return result