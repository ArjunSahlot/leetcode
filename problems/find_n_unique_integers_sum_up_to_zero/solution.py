class Solution:
    def sumZero(self, n: int) -> List[int]:
        sumiszero = []
        if n % 2 == 1:
            sumiszero.append(0)
            if n != 1:
                for i in range(1,(n-1)//2+1):
                    sumiszero.append(i)
                    sumiszero.append(-i)
        else:
            for j in range(1,n//2+1):
                sumiszero.append(j)
                sumiszero.append(-j)
        return sumiszero