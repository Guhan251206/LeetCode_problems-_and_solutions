class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        a=n+k-1
        b=2*k
        mod=10**9+7
        return math.comb(a,b)%mod