class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            f=1
            num=n
            while num>0:
                r=num%10
                f*=r
                num//=10
            if f%t==0:
                return n
            n+=1