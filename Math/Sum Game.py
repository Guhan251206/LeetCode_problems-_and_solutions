class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        mid=n//2
        ls=0
        rs=0
        l=0
        r=0
        for i in range(mid):
            if num[i]=='?':
                l+=1
            else:
                ls+=int(num[i])
        for i in range(mid,n):
            if num[i]=='?':
                r+=1
            else:
                rs+=int(num[i])
        val=2*(ls-rs)+9*(l-r)
        return True if val!=0 else False
