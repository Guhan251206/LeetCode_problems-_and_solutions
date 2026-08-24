class Solution:
    def stoneGameVIII(self, a: List[int]) -> int:
        for i in range(1,len(a)):
            a[i]+=a[i-1]
        best=a[-1]
        for i in range(len(a)-2,0,-1):
            best=max(best,a[i]-best)
        return best