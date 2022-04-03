class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0
        n = 0
        l = len(nums) - 1
        while pos < l:
            if nums[pos] + pos >= l:
                return n + 1
            try:
                possible = [(i, i + nums[i + pos]) for i in range(1, nums[pos]+1)]
            except IndexError:
                return n + 1
            pos += max(possible, key=lambda x: x[1])[0]
            n += 1
        return n
