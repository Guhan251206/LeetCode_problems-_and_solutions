class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        a=[]
        a1=[0]*26
        a2=[0]*26
        for i in p:
            m=ord(i)-97
            a1[m]+=1
        for i in range(len(p)):
            m=ord(s[i])-97
            a2[m]+=1
        if a1==a2:
            a.append(0)
        i=0
        
        while i<(len(s)-len(p)):
            m=ord(s[i])-97
            a2[m]-=1
            n=ord(s[i+len(p)])-97
            a2[n]+=1
            i+=1
        
            if a1==a2:
                a.append(i)
        return a