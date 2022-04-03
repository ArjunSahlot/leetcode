class Solution:
    def maximum69Number (self, nums: int) -> int:
        num = [str(digits) for digits in str(nums)]
        try:
            num[num.index('6')] = '9'
            return ''.join(num)
        except ValueError:
            return nums