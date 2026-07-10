class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp=[0]*(len(nums)-1)
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])
        for i in range(2,len(nums)-1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        d=[0]*(len(nums))
        d[1]=nums[1]
        d[2]=max(nums[1],nums[2])
        for i in range(3,len(nums)):
            d[i]=max(d[i-1],d[i-2]+nums[i])
        
        return max(dp[-1],d[-1])