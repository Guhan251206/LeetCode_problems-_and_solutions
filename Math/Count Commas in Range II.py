class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        count=0
        start=1000
        while start<=n:
            count+=n-start+1
            start*=1000
        return count