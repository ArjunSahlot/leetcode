class Solution:
    def calculate(self, s: str) -> int:
        str = s.replace('/','//')
        return eval(str)