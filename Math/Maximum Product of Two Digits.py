class Solution:
    def maxProduct(self, n: int) -> int:
        a=list(str(n))
        a.sort()
        return int(a[-1])*int(a[-2])