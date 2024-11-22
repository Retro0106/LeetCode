class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new = nums1+nums2
        new.sort()
        if len(new)%2==0:
            a = int(len(new)/2)
            b = int(len(new)/2 -1)
            return (new[a]+new[b])*0.5
        else:
            return new[int((len(new)-1)/2)]