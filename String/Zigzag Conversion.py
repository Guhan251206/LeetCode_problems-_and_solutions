class Solution:
    def convert(self, s: str, k: int) -> str:
        if k==1 or k>=len(s):
            return s
        a=[[] for _ in range(k)]
        inx=0
        d=1
        for i in s:
            a[inx].append(i)
            if inx==0:
                d=1
            if inx==k-1:
                d=-1
            inx+=d
        for i in range(k):
            a[i]="".join(a[i])
        return "".join(a)