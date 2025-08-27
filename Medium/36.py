# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board) -> bool:

        for i in range(9):
            temp = set()
            for j in range(9):
                item = board[i][j]
                if item != ".":
                    if item in temp:
                        return False 
                    temp.add(item)

        for i in range(9):
            temp = set()
            for j in range(9):
                item = board[j][i]
                if item != ".":
                    if item in temp:
                        return False 
                    temp.add(item)

        # checking boxes
        starts =[(0, 0), (0, 3), (0, 6),
                 (3, 0), (3, 3), (3, 6),
                 (6, 0), (6, 3), (6, 6)]

        for i, j in starts:
            temp = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item != ".":
                        if item in temp:
                            return False 
                        temp.add(item)
        return True 