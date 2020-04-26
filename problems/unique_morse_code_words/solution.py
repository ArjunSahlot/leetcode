class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transforms = []
        conversion = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = list('abcdefghijklmnopqrstuvwxyz')
        for i in words:
            transform = []
            for j in i:
                transform.append(conversion[letters.index(j)])
            transforms.append(''.join(transform))
        return len(set(transforms))