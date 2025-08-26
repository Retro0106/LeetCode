class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # i = 0 
        # largest = 0
        # res = ''
        # while i < len(num)-2:
        #     if int(num[i]) == int(num[i+1]) and int(num[i]) == int(num[i+2]):
        #         string = num[i:i+3]
        #         if int(string) >= largest:
        #             res = string
        #             largest = int(string)
        #         i+=2
        #     i+=1
        # return res 

        lis = ["999", "888", '777', '666', '555', '444', '333', '222', '111', '000']
        for a in lis:
            if a in num:
                return a
        return ''