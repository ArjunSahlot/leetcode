class Solution(object):
    def myAtoi(self, str):
        s=""
        sp=str.strip()
        if len(sp)==0:
            return (0)
        if sp[0]=="-":
            y="-"
            sp=sp[1::]
        elif sp[0]=="+":
            y="+"
            sp=sp[1::]
        else:
            y=""
        for a in sp:
            if a.isdigit():
                s+=a
            else:
                break
        print(sp)
        if s=="":
            return (0)
        v=int(y+s)
        if v<(-2**31):
            return (-2**31)
        if  v>=(2**31):
            return (2**31)-1
        if v>-2**31 or v<2**31:
            return v