class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minimal, maximal = float("inf"), float("-inf")
        size, current_size_start_number = 0, None
        for i in range(len(nums)):
            maximal = max(maximal, nums[i])
            minimal = min(minimal, nums[i])
            if abs(maximal - minimal) <= limit: 
                size += 1
            else: # either the nums[i] is too large or too small, which makes the if condition invalid
                current_size_start_number = nums[i-size]
                if current_size_start_number == minimal:
                    minimal = min(nums[i - size + 1:i + 1])
                elif current_size_start_number == maximal:
                    maximal = max(nums[i - size + 1:i + 1])
        
            #print(f"i:{i}, maximal:{maximal}, minimal:{minimal}, size:{size}, current_size_start_num:{current_size_start_number}, maximal:{maximal}, minimal:{minimal}")
        return size   