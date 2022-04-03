class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        list = []
        for i in set(nums):
            if nums.count(i) > len(nums)/3:
                list.append(i)
        return list