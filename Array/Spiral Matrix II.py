class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l=0
        r=n-1
        t=0
        b=n-1
        c=1
        m=[[0]*n for _ in range(n)]
        while l<=r and t<=b:
            for i in range(l,r+1):
                m[t][i]=c
                c+=1
            t+=1
            for i in range(t,b+1):
                m[i][r]=c
                c+=1
            r-=1
            if l<=r and t<=b:
                for i in range(r,l-1,-1):
                    m[b][i]=c
                    c+=1
                b-=1
            if l<=r and t<=b:
                for i in range(b,t-1,-1):
                    m[i][l]=c
                    c+=1
                l+=1
        return m
