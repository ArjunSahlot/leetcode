class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        list = []
        for i in set(nums):
            if nums.count(i) > len(nums)/2:
                list.append(i)
        return max(list)