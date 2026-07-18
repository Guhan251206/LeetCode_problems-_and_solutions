class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1:
            return s
        dp=[[False]*n for i in range(n)]
        l=1
        s1=s[0]
        for i in range(n):
            dp[i][i]=True
            for j in range(i):
                if s[i]==s[j] and (i-j<=2  or dp[j+1][i-1]):
                    dp[j][i]=True
                    if i-j+1>l:
                        l=i-j+1
                        s1=s[j:i+1]
        return s1
    