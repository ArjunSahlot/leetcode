class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        left = nums[:n]
        right = nums[n:]
        
        for i in range(n):
            arr.append(left[i])
            arr.append(right[i])
            
        return arr