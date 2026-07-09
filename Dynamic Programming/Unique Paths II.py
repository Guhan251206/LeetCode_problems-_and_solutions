class Solution:
    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        row=len(a)
        col=len(a[0])
        dp=[[0]*col for _ in range(row)]
        dp[0][0]=1
        for i in range(row):
            for j in range(col):
                if a[i][j]==0:
                    if i>0:
                        dp[i][j]+=dp[i-1][j]
                    if j>0:
                        dp[i][j]+=dp[i][j-1]
                else:
                    dp[i][j]=0
        return dp[-1][-1]