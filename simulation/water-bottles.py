class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        empty = numBottles
        count = numBottles
        exch  = numExchange
        full = 0

        while empty >= exch:
            full = empty // exch
            empty = empty % exch 
            count += full
            empty += full
        return count
        


        
