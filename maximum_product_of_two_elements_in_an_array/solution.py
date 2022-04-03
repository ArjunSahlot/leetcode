class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        high = max(nums) - 1
        nums.remove(max(nums))
        low = max(nums) - 1
        return high * low