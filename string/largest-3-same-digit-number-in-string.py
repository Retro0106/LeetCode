class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0 
        largest = 0
        res = ''
        while i < len(num)-2:
            if int(num[i]) == int(num[i+1]) and int(num[i]) == int(num[i+2]):
                string = num[i:i+3]
                if int(string) >= largest:
                    res = string
                    largest = int(string)
                i+=2
            i+=1
        return res 