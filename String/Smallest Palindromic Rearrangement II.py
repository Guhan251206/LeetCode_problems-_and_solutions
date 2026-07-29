from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        limit=10**6+1
        def prem(half):
            t1=sum(half.values())
            ans=1
            rem=t1
            for c in half.values():
                if c: 
                    ans*=comb(rem,c)
                    rem-=c
                    if ans>limit:
                        return limit
            return ans

        cnt=Counter(s)
        half={}
        mid=''
        for ch in sorted(cnt):
            half[ch]=cnt[ch]//2
            if cnt[ch]%2==1:
                mid=ch
        if prem(half)<k:
            return ""
        t=sum(half.values())
        l=[]
        for _ in range(t):
            for ch in sorted(half):
                if half[ch]==0:
                    continue
                half[ch]-=1
                way=prem(half)
                if way>=k:
                    l.append(ch)
                    break
                else:
                    k-=way
                    half[ch]+=1
        left="".join(l)
        return left+mid+left[::-1]

