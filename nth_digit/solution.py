class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        n_ = n
        k = 1
        while n_ > k * (10**k - 10**(k-1)):
            n_ -= k * (10**k - 10**(k-1))
            k += 1
        k_ = (n_ - 1) // k 
        num = 10**(k-1) + k_
        return int(str(num)[n_ - 1 - k_ * k])