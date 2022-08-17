class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookup = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = []
        for w in words:
            trans.append("".join(list(map(lambda x: lookup[ord(x)-97], w))))
        return len(set(trans))