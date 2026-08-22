class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p=1
        s=0
        t=n
        while n>0:
            s+=n%10
            p*=n%10
            n//=10
        return t%(s+p)==0