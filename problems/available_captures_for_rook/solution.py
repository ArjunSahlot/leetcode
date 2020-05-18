class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        attacks_possible = 0
        vert = []
        for i in board:
            if "R" in i:
                horiz = i
                b_ind = i.index("R")
                break
        for j in board:
            vert.append(j[b_ind])
        fil_vert = [x for x in vert if x != "."]
        fil_horiz = [y for y in horiz if y != "."]
        if "pR" in ''.join(fil_vert):
            attacks_possible += 1
        if "Rp" in ''.join(fil_vert):
            attacks_possible += 1
        if "pR" in ''.join(fil_horiz):
            attacks_possible += 1
        if "Rp" in ''.join(fil_horiz):
            attacks_possible +=1 
        return attacks_possible