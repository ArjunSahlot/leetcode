class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        table = {}
        for i in arr:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        cursum = 0
        curr = 0
        for i in sorted(table.values(), reverse=True):
            curr += 1
            cursum += i
            if cursum >= len(arr)//2:
                return curr