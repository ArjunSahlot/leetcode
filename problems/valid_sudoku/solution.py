class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row = "".join(row).replace(".", "")
            if len(row) != len(set(row)):
                return False
        for c in range(9):
            col = [board[r][c] for r in range(9) if board[r][c] != "."]
            if len(col) != len(set(col)):
                return False
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = [board[row][col] for row in range(r, r+3) for col in range(c, c+3) if board[row][col] != "."]
                if len(box) != len(set(box)):
                    return False
        
        return True
