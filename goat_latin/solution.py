class Solution:
    def toGoatLatin(self, S: str) -> str:
        string = S.split()
        ans = ""
        for wordind in range(len(string)):
            if string[wordind].lower().startswith('a') or string[wordind].lower().startswith('e') or string[wordind].lower().startswith('i') or string[wordind].lower().startswith('o') or string[wordind].lower().startswith('u'):
                ans = ans + string[wordind] + "ma"
            else:
                ans = ans + string[wordind][1:] + string[wordind][:1] + "ma"
            ans = ans + "a" * (wordind + 1)
            ans = ans + " "
        ans = ans.strip()
        return ans