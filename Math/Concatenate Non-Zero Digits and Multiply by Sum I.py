class Solution:
    def sumAndMultiply(self, n: int) -> int:
        i=0
        x=s=0
        while n>0:
            r=n%10
            s+=r
            if r!=0:
                x+=r*(10**i)
                i+=1
            n//=10
        return s*x