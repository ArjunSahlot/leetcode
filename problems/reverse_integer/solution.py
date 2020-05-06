class Solution(object):
    def reverse(self, x):
        x_str = str(x)
        flg = True
        
        if x < 0:  
          x_str = x_str[1:]
          flg = False
            
        rev_ = x_str[::-1]
        if not flg:
          rev_ = "-" + rev_
        
        rev_ = int(rev_)
        return rev_ if -2147483648 <= rev_ <= 2147483647 else 0