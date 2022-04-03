from collections import OrderedDict
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {indices[i] : s[i] for i in range(len(s))}
        return "".join(OrderedDict(sorted(dict.items())).values())
