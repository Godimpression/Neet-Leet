class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=abs(x)
            x=str(x)
            z=x[-1::-1]
            if -2**31 < (int(z)*-1):
                return int(z)*-1
            else:
                return 0
        else:
            x=str(x)
            x=x[-1::-1]
            if -2**31 < int(x) < 2**31-1:
                
                return int(x)
            else:
                return 0
        
