class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        strs = ''.join([str(num) for num in nums])
        for i in range(0,k):
            string = '1' + '0'*i + '1'
            if string in strs:
                return False
        return True