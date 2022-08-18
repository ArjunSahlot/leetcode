class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        table = {}
        for i in arr:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        cursum = 0
        for i, val in enumerate(sorted(table.values(), reverse=True)):
            cursum += val
            if cursum >= len(arr)//2:
                return i+1