class Solution:
    def smallestPalindrome(self, s: str) -> str:
        f=[0]*26
        for i in s:
            f[ord(i)-ord('a')]+=1
        n=len(s)
        a=['']*n
        l=0
        r=n-1
        for i in range(len(f)):
            while f[i]>=2:
                a[l]=chr(ord('a')+i)
                a[r]=chr(ord('a')+i)
                f[i]-=2
                l+=1
                r-=1
            if f[i]==1:
                a[n//2]=chr(ord('a')+i)
        return "".join(a)