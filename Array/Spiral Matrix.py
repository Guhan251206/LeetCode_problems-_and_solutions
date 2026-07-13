class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        a=[]
        l=0
        r=len(m[0])-1
        t=0
        b=len(m)-1
        while l<=r and t<=b:
            for i in range(l,r+1):
                a.append(m[t][i])
            t+=1
            for i in range(t,b+1):
                a.append(m[i][r])
            r-=1
            if l<=r and t<=b:
                for i in range(r,l-1,-1):
                    a.append(m[b][i])
                b-=1
            if l<=r and t<=b:
                for i in range(b,t-1,-1):
                    a.append(m[i][l])
                l+=1
        return a
