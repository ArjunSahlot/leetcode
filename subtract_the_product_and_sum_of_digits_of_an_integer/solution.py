import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = [int(digits) for digits in str(n)]
        return math.prod(num)-sum(num)