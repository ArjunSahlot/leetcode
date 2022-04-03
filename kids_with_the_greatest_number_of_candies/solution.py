class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        bignum = max(candies)
        for i in candies:
            if i + extraCandies >= bignum:
                output.append(True)
            else:
                output.append(False)
        return output