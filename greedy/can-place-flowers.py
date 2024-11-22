class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        count = 0
        i = 0
        if not flowerbed:
            return False
        elif len(flowerbed)<2:
            if n < 2 and flowerbed[0]==0:
                return True
            elif n==0 and flowerbed[0]==1:
                return True
            

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        count+=1 
                        flowerbed[i]=1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        count+=1 
                        flowerbed[i]=1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        count+=1 
                        flowerbed[i]=1
            i+=1
        return n <= count