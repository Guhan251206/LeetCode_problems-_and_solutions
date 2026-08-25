class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        @cache
        def dfs(i,s):
            if i==len(nums):
                if s==target:
                    return 1
                return 0
            p=dfs(i+1,s+nums[i])
            n=dfs(i+1,s-nums[i])
            return p+n
        return dfs(0,0)
        