class Solution:
    def reverse(self, x: int) -> int:
        if x>(2**31)-1 or x<(-2**31):
            return 0
        print(2**31)
        if x<0:
            a=str(x)[1:]
            x='-'+a[::-1]
            return int(x) if int(x)>(-2**31) else 0
        return int(str(x)[::-1]) if int(str(x)[::-1])<(2**31) else 0