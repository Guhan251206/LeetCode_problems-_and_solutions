class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        print(nums)
        def back(i,k,path):
            if k==0:
                ans.append(path.copy())
                return 
            if i>=n or k<0:
                return 
            for j in range(i,n):
                if j>i and nums[j]==nums[j-1]:
                    continue
                if nums[j]>k:
                    break
                path.append(nums[j])
                back(j+1,k-nums[j],path)
                path.pop()
        back(0,target,[])
        return ans