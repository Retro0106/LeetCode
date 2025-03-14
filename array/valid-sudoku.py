from collections import Counter
import copy
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checker(matrix):
            for i in range(len(matrix)):
                hashmap = Counter(matrix)
                for key in hashmap:
                    if hashmap[key] > 1 and key != '.':
                        return False
            return True
        
        for i in range(len(board)):
            if not checker(board[i]):
                return False

        board2 = copy.deepcopy(board)
        board3 = [[row[i] for row in board2] for i in range(len(board2[0]))]

        for i in range(len(board3)):
            if not checker(board3[i]):
                return False
        
        for i in range(0, len(board), 3):
            arr = []
            for j in range(0, len(board[i]), 3):
                arr.append(board[i][j])
            if not checker(arr):
                return False
        return True
        
