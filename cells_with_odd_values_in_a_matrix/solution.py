class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0] * m for _ in range(n)]
        for row, col in indices:
            for i in range(len(matrix[row])):
                matrix[row][i] += 1
            for i in range(len(matrix)):
                matrix[i][col] += 1
        count = 0
        for row in matrix:
            for value in row:
                if value % 2 == 1:
                    count += 1
        return count