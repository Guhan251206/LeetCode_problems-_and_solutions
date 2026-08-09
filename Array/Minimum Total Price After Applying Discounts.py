class Solution:
    def minPrice(self, p: list[int], d: list[int]) -> float:
        p.sort()
        d.sort()
        p=p[::-1]
        d=d[::-1]
        j=0
        for i in range(len(p)):
            if j<len(d):
                p[i]=(p[i]*(100-d[j]))/100
                j+=1
        return sum(p)