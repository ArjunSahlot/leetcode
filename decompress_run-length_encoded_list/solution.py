class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        splitlist = [nums[i * 2:(i + 1) * 2] for i in range((len(nums) + 2 - 1) // 2 )]
        finallist = []
        for freq, value in splitlist:
            for i in range(freq):
                finallist.append(value)
        return finallist