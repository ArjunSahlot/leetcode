class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 0
        currentlen = 1
        if nums == [1]:
            return 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currentlen += 1
            else:
                currentlen = 1
            if longest < currentlen:
                longest = currentlen
        return longest