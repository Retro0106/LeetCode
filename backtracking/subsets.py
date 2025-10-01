class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        n = len(nums)
        
        def backtracking(i):
                if i == len(nums):
                    result.append(curr[:])
                    return
                
                curr.append(nums[i])
                backtracking(i+1)

                curr.pop()
                backtracking(i+1)

        backtracking(0)
        return result

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # res = []
        # curr = []

        # def dfs(i):
        #     if i == len(nums):
        #         res.append(curr[:])
        #         return
            
        #     curr.append(nums[i])
        #     dfs(i+1)
        #     curr.pop()

        #     dfs(i+1)
        # dfs(0)
        # return res