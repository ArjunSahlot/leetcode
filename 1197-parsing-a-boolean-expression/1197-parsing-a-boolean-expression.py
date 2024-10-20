class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return expression == 't'
        
        if expression[0] == '!':
            return not self.parseBoolExpr(expression[2:-1])
        
        # split by points that are outside the ()s
        values = [""]

        lefts = 0
        for i in range(2, len(expression)-1):
            if expression[i] == '(': lefts += 1
            elif expression[i] == ')': lefts -= 1
            if lefts == 0 and expression[i] == ',':
                values.append("")
            else:
                values[-1] += expression[i]

        if expression[0] == '&':
            return all(map(self.parseBoolExpr, values))
        
        if expression[0] == '|':
            return any(map(self.parseBoolExpr, values))
