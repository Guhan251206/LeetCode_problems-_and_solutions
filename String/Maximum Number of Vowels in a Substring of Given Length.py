class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        m=0
        for i in range(k):
            if s[i] in "aeiou":
                c+=1
        m=c
        i=0
        j=k
        if m==k:
            return m
        while i<len(s)-k:
            if s[i] in 'aeiou':
                c-=1
            if s[j] in 'aeiou':
                c+=1
            m=max(m,c)
            
    
            i+=1
            j+=1
        return m