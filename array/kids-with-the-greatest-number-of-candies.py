class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = max(candies)
        candies = [candies[i]+extraCandies>= maximum for i in range(len(candies))]
        return candies
        # for i in range(len(candies)):
        #     candies[i] = candies[i] + extraCandies >= maximum
        # return candies
        
        
        
        
        
        # maximum = 0
        # for i in candies:
        #     if i > maximum:
        #         maximum = i
        # for i in range(len(candies)):
        #     if candies[i] + extraCandies >= maximum:
        #         candies[i] = True
        #     else:
        #         candies[i] = False
        # return candies