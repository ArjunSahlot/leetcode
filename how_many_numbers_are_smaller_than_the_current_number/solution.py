class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        finallist = []
        num = 0
        for i in nums:
            for j in nums:
                if j < i:
                    num += 1
            finallist.append(num)
            num = 0
        return finallist