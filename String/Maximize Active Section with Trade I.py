class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        one=s.count('1')
        a=[]
        s1='1'+s+'1'
        for i in s1.split('1'):
            if i:
                a.append(len(i))
        if len(a)<2:
            return one
        b=0
        for i in range(len(a)-1):
            b=max(b,a[i]+a[i+1])
        return one+b