from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        fre=Counter(word)
        fq=dict(sorted(fre.items(),key=lambda x:x[1], reverse=True))
        i1=0
        cnt=0
        c1=1
        for key in fq:
            
            cnt+=(c1*fq[key])
            i1+=1
            if i1%8==0:
                c1+=1
        return cnt