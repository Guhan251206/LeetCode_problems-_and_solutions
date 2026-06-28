class Solution:
    def titleToNumber(self, n: str) -> int:
        
        n=list(n)
        i=0
        s=0
        while len(n)>0:
            ch=n.pop()
            s+=(ord(ch)-64)*(26**i)
            i+=1

        return s