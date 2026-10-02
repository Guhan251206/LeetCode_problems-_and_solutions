class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp=[0]*k
        ans=[0]*k
        for x in nums:
            i=x%k
            temp=[0]*k
            temp[i]+=1
            for j in range(k):
                temp[(j*i)%k]+=dp[j]
            dp=temp
            for j in range(k):
                ans[j]+=dp[j]
        return ans