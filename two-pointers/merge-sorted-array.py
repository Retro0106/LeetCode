class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j-=1
            k-=1

        
        
        
        
        
        
        
        
        
        # a = m+n-1
        # for i in range(n-1,-1,-1):
        #     nums1[a] = nums2[i]
        #     a-=1
        # nums1.sort()

        # j = m
        # i = 0
        # while i < j and j < m+n:
        #     if not nums1[i] > nums1[j]:
        #         i += 1
        #         continue
        #     while nums1[i] > nums1[j]:
        #         nums1[i], nums1[j] = nums1[j], nums1[i]
        #         i+=1
        #     j+=1
                
            
        










        # j = i = 0
        # while j < n:
        #     if nums2[j] <= nums1[i] or i >= m+j:
        #         nums1.insert(i,nums2[j])
        #         j+=1
        #         nums1.pop()
        #     i+=1




        # j = 0
        # for i in range(m):
        #     if j == n-1:
        #         break
        #     if nums2[j] <= nums1[i]:
        #         nums1.insert(i,nums2[j])
        #         j += 1
            

            
            