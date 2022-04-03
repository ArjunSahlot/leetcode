class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        brr = []
        for i in set(arr):
            brr.append(arr.count(i))
        if sorted(set(brr)) == sorted(brr):
            return True
        return False