class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        if s>9*n:
            return -1
        a=[9]*n
        f=False
        for i in range(n-1,-1,-1):
            for j in range(9,-1,-1):
                a[i]=j
                if sum(a)==s:
                    f=True
                    break
                if sum(a)>s:
                    continue
                if sum(a)<s:
                    a[i]=a[i]+1
                    break
            if f:
                break
        if sum(a)!=s:
            return -1
        r=a[0]
        for i in range(1,n):
            r=r*10+a[i]
        return r