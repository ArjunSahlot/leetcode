class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distval = 0
        for i in arr1:
            distval += 1
            for j in arr2:
                if abs(i - j) > d:
                    continue
                else:
                    distval -= 1
                    break
        return distval