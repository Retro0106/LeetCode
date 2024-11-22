class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # i = 0
        # j = len(height)-1
        # maximum = min(height[i],height[j]) * (j-i)
        # while i < j:
        #     area = height
        #     if height[i+1] > height[i] 























        left = 0
        right = len(height) - 1
        maximum = curr = 0
        while left < right:
            curr = min(height[left],height[right])*(right-left)
            maximum = max(curr,maximum)
            if height[left] >= height[right]:
                right -= 1
            else:
                left+=1
        return maximum




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # curr = maximum = 0
        # left = 0
        
        # while left < len(height)-1:
        #     right = left + 1
        #     while right < len(height):
        #         if height[left] < height[right]:
        #             curr = height[left] * (right-left)
                    
        #         else:
        #             curr = height[right] * (right-left)

        #         if curr > maximum:
        #             maximum = curr
        #         right += 1
        #     left += 1
        # return maximum
                


            
            

            