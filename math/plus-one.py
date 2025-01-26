class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # number = ''
        # for num in digits:
        #     number += str(num)
        # number = int(number)

        # number += 1
        # res = []
        # for num in str(number):
        #     res.append(int(num))
        # return res

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
