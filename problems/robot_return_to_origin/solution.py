class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R'):
            return True
        else:
            return False