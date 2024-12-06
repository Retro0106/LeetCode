class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = float('inf')
        maxProfit = 0
        for num in prices:
            minimum = min(minimum, num)
            profit = num - minimum
            maxProfit = max(maxProfit, profit)
        return maxProfit
        
        
        # minimum = float('inf')        
        # max_profit = 0
        # for price in prices:
        #     minimum = min(minimum,price)
            
        #     profit = price - minimum
        #     max_profit = max(profit,max_profit)
        # return max_profit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(prices)<2:
        #     return 0
        # maxProfit = []
        # for i in range(len(prices)-1):
        #     if i+1 < len(prices)-1:
        #         if i <= max(prices[i+1:]):
        #             profit = max(prices[i+1:]) - prices[i]
        #             maxProfit.append(profit)
        # if max(maxProfit)<=0:
        #     return 0
        # return max(maxProfit)




        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         maxProfit.append(profit)
        # if max(maxProfit)<=0:
        #     return 0
        # return max(maxProfit)