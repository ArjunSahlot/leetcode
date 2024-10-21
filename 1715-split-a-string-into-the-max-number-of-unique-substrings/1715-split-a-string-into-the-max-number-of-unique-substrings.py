class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        big = float("-inf")
        for i in range(pow(2, len(s)-1)):
            segments = [""]
            binary = bin(i)[2:]
            binary = "0"*(len(s)-len(binary)-1) + binary
            for ind in range(len(s)):
                segments[-1] += s[ind]
                if ind < len(binary) and binary[ind] == "1":
                    segments.append("")
            
            if len(segments) == len(set(segments)):
                big = max(big, len(segments))
        
        return big
