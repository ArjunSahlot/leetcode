class Solution:
    def selfDividingNumbers(self, st: int, ed: int) -> List[int]:
        final = []
        for num in range(st, ed+1):
            count = 0
            numlst = [int(digits) for digits in str(num)]
            for i in numlst:
                if i != 0 and num % i == 0:
                    count += 1
            if count == len(numlst):
                final.append(num)
        return final