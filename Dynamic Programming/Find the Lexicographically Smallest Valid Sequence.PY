class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n=len(word1)
        m=len(word2)
        dp=[-1]*m
        i=n-1
        j=m-1
        while i>=0 and j>=0:
            if word1[i]==word2[j]:
                dp[j]=i
                j-=1
            i-=1
        ans=[]
        f=True
        j=0
        for i in range(n):
            if j==m:
                break
            if word1[i]==word2[j]:
                ans.append(i)
                j+=1
            elif f and (j==m-1 or i<dp[j+1]):
                f=False
                ans.append(i)
                j+=1
        if j==m:
            return ans
        return []