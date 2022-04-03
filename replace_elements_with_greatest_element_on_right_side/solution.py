class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rmax, output = 0, [-1]
        for i in range(len(arr)-1, 0, -1):
            if arr[i] > rmax:
                rmax = arr[i] 
        #   output[i-1] = rmax
        # return output
            output.insert(0, rmax)
        return output