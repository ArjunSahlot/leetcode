import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        answer = math.log(n, 4)
        return (answer - answer // 1) < 0.001