class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for i in J:
            jewels += S.count(i)
        return jewels