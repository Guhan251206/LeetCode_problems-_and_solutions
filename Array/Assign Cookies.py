class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=j=0
        g.sort()
        s.sort()
        for i in range(len(g)):
            while j<len(s):
                if g[i]<=s[j]:
                    c+=1
                    j+=1
                    break
                j+=1
        return c