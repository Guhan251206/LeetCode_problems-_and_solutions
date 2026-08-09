class Solution:
    def addDigits(self, num: int) -> int:
        def fun(x):
            sum=0
            while x>0:
                sum+=x%10
                x//=10
            return sum
        while num>9:
            num=fun(num)
        return num