class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        p = re.compile(p)
        m = p.match(s)
        if not m:
            return False
        if m.group() == s:
            return True
        return False
        