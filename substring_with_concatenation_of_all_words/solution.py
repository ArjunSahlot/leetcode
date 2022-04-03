class Solution:
    
    @staticmethod
    def possible(words, l):
        for w in words:
            if w.startswith(l):
                return True
        return False

    @staticmethod
    def all_match(words, s, ind, l):
        line = s[ind:ind+l*len(words)]
        parts = [line[i:i+l] for i in range(0, len(line), l)]
        if len(parts) != len(words):
            return False
        for w in words:
            if w not in parts:
                return False
            parts.remove(w)

        return True

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        final = []
        for i in range(0, len(s)):
            if Solution.possible(words, s[i]):
                if Solution.all_match(words, s, i, l):
                    final.append(i)

        return final
