class Solution:
    def longestPalindrome(self, s: str) -> int:
        fre={}
        for x in s:
            fre[x]=fre.get(x,0)+1
        f=False
        n=0
        for k,x in fre.items():
            while x>1:
                n+=2
                x-=2
            if x==1:
                f=True
        if f:
            n+=1
        return n