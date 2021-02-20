from copy import deepcopy


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_empty():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        return i, j
            return False

        def valid(d, row, col):
            for i in range(9):
                if board[row][i] == d and i != col:
                    return False
            for i in range(9):
                if board[i][col] == d and i != row:
                    return False
            br, bc = (row // 3) * 3, (col // 3) * 3
            for r in range(br, br+3):
                for c in range(bc, bc+3):
                    if board[r][c] == d and r != row and c != col:
                        return False
            
            return True

        pos = get_empty()
        if pos:
            row, col = pos
        else:
            return True
        
        for d in [str(i) for i in range(1, 10)]:
            if valid(d, row, col):
                board[row][col] = d
                
                if self.solveSudoku(board):
                    return True
                
                board[row][col] = "."
        
        return False
