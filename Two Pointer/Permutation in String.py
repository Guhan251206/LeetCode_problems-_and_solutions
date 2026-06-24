class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1=[0]*26
        a2=[0]*26
        if len(s1)>len(s2):
            return False
        for i in s1:
            m=ord(i)-97
            a1[m]+=1

        for i in range(len(s1)):
            m=ord(s2[i])-97
            a2[m]+=1
        if a1==a2:
            return True

        i=0
        
        while i<(len(s2)-len(s1)):
            m=ord(s2[i])-97
            a2[m]-=1
            m=ord(s2[i+len(s1)])-97
            a2[m]+=1
            i+=1
            
            if a1==a2:
                return True
        return False