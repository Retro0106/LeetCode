class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initialize i as 0
        # loop through matrix(use while loop) - while i < len(matrix)
        # in while loop set left as 0, right as len(matrix[i])
        # check if target is in this range
            # if it is
                # binary search while loop: while left <= right
                # if target is there return True
                # if not return False
            # if not i += 1
        # outside while loop: return False


        i = 0
        while i < len(matrix):
            left, right = 0, len(matrix[i])-1
            if matrix[i][left] <= target <= matrix[i][right]:
                while left <= right:
                    mid = (left+right) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
            else:
                i += 1
        return False


