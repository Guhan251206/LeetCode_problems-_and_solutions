class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        if k>=0:
            s=0
            for i in range(k):
                s+=code[i]
            j=k
            a=[]
        
            for i in range(len(code)):
                s-=code[i]
                s+=code[j%len(code)]
                j+=1
                a.append(s)
        else:
            a=[]
            for i in range(len(code)):
                s=0
                t=k
                j=i-1
                while t!=0:
                    s+=code[j]
                    j-=1
                    t+=1
                a.append(s)
        return a