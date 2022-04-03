class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        first = []
        second = []
        for x,y in paths:
            first.append(x)
            second.append(y)
        for i in set(second):
            if i not in first:
                return i