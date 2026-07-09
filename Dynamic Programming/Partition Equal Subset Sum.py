class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        t=sum(nums)//2
        dp=[[False]*(t+1) for _ in range(len(nums))]
       
        if t>=nums[0]:
            dp[0][nums[0]]=True
        dp[0][0]=True
        for i in range(len(nums)):
            for j in range(t+1):    
                if i>0:
                    if dp[i-1][j]==True:
                        dp[i][j]=True
                if j>=nums[i] and i>0:
                    if dp[i-1][j-nums[i]]==True:
                        dp[i][j]=True
            
            
        return dp[-1][-1]