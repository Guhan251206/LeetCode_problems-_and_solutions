class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        a=[]
        for k in range(2,len(s)+1):
            l=0
            r=k
            while r<10:
                ch=s[l:r]
                a.append(int(ch))
                l+=1
                r+=1
        b=[]
        for i in a:
            if low<=i and high>=i:
                b.append(i)
            if i>high:
                break
        return b