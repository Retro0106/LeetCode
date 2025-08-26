class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest_diagonal = 0
        maximum_area = 0
        
        for dimension in dimensions:
            a,b = dimension
            diagonal = a**2 + b**2
            if diagonal > longest_diagonal:
                longest_diagonal = diagonal
                maximum_area = a*b
            elif diagonal == longest_diagonal:
                maximum_area = max(maximum_area, a*b)
        return maximum_area
