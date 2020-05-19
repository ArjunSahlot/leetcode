class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nums = []
        for i in set(arr):
            if i == arr.count(i):
                nums.append(i)
        if nums == []:
            return -1
        else:
            return max(nums)