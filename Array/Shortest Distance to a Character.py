class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i]==c:
                a.append(i)
        for i in range(len(s)):
            m=10**10
            for j in a:
                if m>abs(i-j):
                    m=abs(i-j)
            b.append(m)
        return b