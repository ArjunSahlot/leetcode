class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        popen, output = 0, []
        for i in S:
            if i == ')':
                popen -= 1
            if popen > 0:
                output.append(i)
            if i == '(':
                popen += 1
        return ''.join(output)