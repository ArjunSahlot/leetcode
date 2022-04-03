class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return ''.join([str(i) for item in grid for i in item]).count('-')