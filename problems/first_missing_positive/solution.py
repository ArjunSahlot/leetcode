class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [i for i in set(nums) if i > 0]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        if nums:
            return nums[-1] + 1
        else:
            return 1
