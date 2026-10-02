class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        ans=-1
        target=sum(nums)
        target-=x
        sum1=0
        l=0
        r=0
        while r<len(nums):
            sum1+=nums[r]
            while sum1>target and l<=r:
                sum1-=nums[l]
                l+=1
            if sum1==target:
                ans=max(ans,r-l+1)
            r+=1
        if ans==-1:
            return -1
        return len(nums)-ans