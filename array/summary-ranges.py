class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        i = 0
        
        if len(nums)<1:
            return nums
        elif len(nums)==1:
            nums[0] = str(nums[0])
            return nums
        a = b = nums[i]
        while i < len(nums):
            b = nums[i]
            if i+1 < len(nums):
                if b+1 != nums[i+1]:
                    if a == b:
                        output.append(str(a))
                    else:
                        output.append(str(a)+'->'+str(b))
                    i+=1
                    a = b = nums[i]
                else:
                    i+=1
            else:
                if b+1 != nums[i]:
                    if a == b:
                        output.append(str(a))
                    else:
                        output.append(str(a)+'->'+str(b))
                    i+=1
                    a = b = nums[i-1]
                else:
                    i+=1
        return output
            

            

            