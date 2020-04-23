class Solution:
    def isPalindrome(self, s: str) -> bool:
        if ''.join(x.lower() for x in s if x.isalnum()) == ''.join(y.lower() for y in s if y.isalnum())[::-1]:
            return True
        else:
            return False