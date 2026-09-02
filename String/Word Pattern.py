class Solution:
    def wordPattern(self, t: str, s: str) -> bool:
        a=s.split()
        if len(a)!=len(t):
            return False
        d1={}
        d2={}
        for i in range(len(a)):
            if t[i] in d1 and d1[t[i]]!=a[i]:
                return False
            if a[i] in d2 and d2[a[i]]!=t[i]:
                return False
            d1[t[i]]=a[i]
            d2[a[i]]=t[i]
        return True