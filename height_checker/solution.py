class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        moves = 0
        for i in range(len(heights)):
            if heights[i] != sorted(heights)[i]:
                moves += 1
        return moves