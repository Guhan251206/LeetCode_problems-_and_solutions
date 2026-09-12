class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def back(sum,i,path):
            if sum==target:
                cur=path.copy()
                ans.append(cur)
                return 
            if sum>target or i>=n:
                return
            path.append(nums[i])
            back(sum+nums[i],i,path)
            path.pop()
            back(sum,i+1,path)
        back(0,0,[])
        return ans