class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        c=0
        for i in range(k):
            if blocks[i]=='W':
                c+=1
        m=c
        l=0
        r=k
        while l<len(blocks)-k:
            if blocks[l]=='W':
                c-=1
            if blocks[r]=='W':
                c+=1
            l+=1
            r+=1
            m=min(m,c)
        return m