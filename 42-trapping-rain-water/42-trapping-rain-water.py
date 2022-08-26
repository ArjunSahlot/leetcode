class Solution:
    def trap(self, height: List[int]) -> int:
        left = [-1]
        right = [-1]
        
        for h in height:
            if left[-1] < h:
                left.append(h)
            else:
                left.append(left[-1])
        
        left.pop(0)
        
        for h in reversed(height):
            if right[0] < h:
                right.insert(0, h)
            else:
                right.insert(0, right[0])
        
        right.pop(-1)

        trapped = 0
        for i, h in enumerate(height):
            trapped += min(left[i], right[i])-h
        
        return trapped