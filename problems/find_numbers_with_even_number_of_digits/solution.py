class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        enums = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                enums += 1
        return enums