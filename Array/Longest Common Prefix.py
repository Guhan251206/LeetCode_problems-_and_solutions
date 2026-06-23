class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        b=''
        m=strs[0]
        n=len(m)
        for i in strs:
            if len(i)<n:
                n=len(i) 
        for i in range(n):
            f=0
            for a in strs:
                if m[i]!=a[i]:
                    f=1
                    break
            if f==0:
                b+=m[i]
            else:
                break
        return b