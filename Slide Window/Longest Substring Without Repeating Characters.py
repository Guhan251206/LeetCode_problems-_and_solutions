class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        m=0
        a=set()
        for r in range(len(s)):
            if s[r] in a:
                while s[r] in a:
                    a.discard(s[l])
                    l+=1
            a.add(s[r])
            m=max(m,len(a))
        return m
