class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0 or n>2**31:
            return False
        print(-2**31)
        while n>1:
            if n%4!=0:
                return False
            n//=4
        return True