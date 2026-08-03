class Solution:
    def stoneGameIII(self,arr: List[int]) -> str:
        n=len(arr)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            m=float('-inf')
            cur=0
            for k in range(1,4):
                if i+k>n:
                    break
                cur+=arr[i+k-1]
                m=max(m,cur-dp[i+k])
            dp[i]=m
        if dp[0]>0:
            return "Alice"
        if dp[0]<0:
            return "Bob"
        if dp[0]==0:
            return "Tie"