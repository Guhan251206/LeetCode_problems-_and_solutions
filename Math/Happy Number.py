class Solution:
    def isHappy(self, z: int) -> bool:
        def fun(n):
            if (n==1 or n==7):
                return True
            if n<10:
                return False
            
            sum=0
            while n>0:
                r=n%10
                sum+=r*r
                n//=10
            return fun(sum)
        return fun(z)