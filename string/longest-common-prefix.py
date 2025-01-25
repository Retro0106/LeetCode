class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        left = strs[0]
        right = strs[len(strs)-1]
        res = ''
        for i in range(len(left)):
            if left[i] != right[i]:
                return res
            res += left[i]




        # i = 0
        # j = 0
        # k = 1
        # new = ''
        # if len(strs) == 1:
        #     new = new + strs[0]
        #     return new
        # while len(strs) > 1 and i < len(strs)and j < len(min(strs)):
        #     while k<len(strs):
        #         if strs[0][j] != strs[k][j]:
        #             return new
        #         else:
        #             k+=1
        #     new+=strs[0][j]
        #     j+=1 
        #     k=1
        # return new
        
                    
                

        