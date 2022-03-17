class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == "":
            return s
        
        curr = 0
        new_str = ""
        
        for i, l in enumerate(s):
            if l == ")":
                if curr == 0:
                    continue
                curr -= 1
            if l == "(":
                curr += 1
            new_str += l
    
        if curr:
            new_str = list(new_str)[::-1]
            for _ in range(curr):
                new_str.remove("(")
            new_str = "".join(new_str)[::-1]
        
        return new_str
