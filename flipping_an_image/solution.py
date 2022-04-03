class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        final = []
        for i in A:
            final.append([1 if x == 0 else 0 for x in reversed(i)])
        return final