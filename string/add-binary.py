class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

        # def decimal(string):
        #     j = 0
        #     total = 0
        #     for i in range(len(string)-1, -1, -1):
        #         total += int(string[i]) * (2 ** j)
        #         j += 1
        #     return total
        
        # def binary(num):
        #     number = ''
        #     while num != 1:
        #         if num % 2 == 0:
        #             number = '0' + number
        #         else:
        #             number = '1' + number
        #         num = num // 2
        #     number = '1' + number
        #     return number
        
        # return binary(decimal(a) + decimal(b))


        