class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        INF=float('inf')
        dp=[[INF]*(amount+1) for i in range(len(coins))]
        
        dp[0][0]=0
        for i in range(len(coins)):
            for j in range(amount+1):
                
                if i>0:
                    dp[i][j]=min(dp[i][j],dp[i-1][j])
                if j>=coins[i]:
                    dp[i][j]=min(dp[i][j],1+dp[i][j-coins[i]])
        if dp[-1][-1]==INF:
            return -1
        return dp[-1][-1]