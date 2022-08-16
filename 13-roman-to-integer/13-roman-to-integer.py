class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "a").replace("IX", "b").replace("XL", "c").replace("XC", "d").replace("CD", "e").replace("CM", "f")
        return s.count("a")*4+s.count("b")*9+s.count("c")*40+s.count("d")*90+s.count("e")*400+s.count("f")*900+s.count("I")+s.count("V")*5+s.count("X")*10+s.count("L")*50+s.count("C")*100+s.count("D")*500+s.count("M")*1000