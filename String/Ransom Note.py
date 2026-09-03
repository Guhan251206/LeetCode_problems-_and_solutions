class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        fre={}
        for ch in m:
            fre[ch]=fre.get(ch,0)+1
        
        for ch in r:
            n=fre.get(ch,0)
            print(n)
            if n==0:
                return False
            fre[ch]=n-1
        return True