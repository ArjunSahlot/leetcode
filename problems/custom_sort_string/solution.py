class Solution:
    def customSortString(self, S: str, T: str) -> str:
        return "".join([l*T.count(l) for l in S]) + "".join([l for l in T if l not in S])
