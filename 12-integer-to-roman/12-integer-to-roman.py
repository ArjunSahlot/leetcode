class Solution:
    def intToRoman(self, num: int) -> str:
        table = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]

        string = ""

        while num != 0:
            for v in table:
                if v[1] <= num:
                    string += v[0]
                    num -= v[1]
                    break

        return string