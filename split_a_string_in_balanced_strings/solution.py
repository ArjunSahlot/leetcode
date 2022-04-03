class Solution:
    def balancedStringSplit(self, s: str) -> int:
        substrings = 0
        rcount = 0
        lcount = 0
        for ch in s:
            if ch == 'R':
                rcount += 1
            else:
                lcount += 1
            if rcount == lcount:
                substrings += 1
                rcount = 0
                lcount = 0
        return substrings