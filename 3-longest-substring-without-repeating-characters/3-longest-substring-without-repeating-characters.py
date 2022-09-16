class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        charpos = {}
        
        start = 0
        end = 0
        curmax = 0
        while start < len(s):
            if end == len(s):
                return max(curmax, end-start)
            if s[end] in charpos:
                curmax = max(curmax, end-start)
                start = charpos[s[end]]+1
                end = start
                charpos = {}
                continue

            charpos[s[end]] = end
            
            end += 1
        
        return curmax