class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return max(nums)
        fre={}
        l=0
        for r in range(k,len(nums)+1):
            for i in range(l,r):
                fre[nums[i]]=fre.get(nums[i],0)+1
            l+=1
        m=-1
        for key,x in fre.items():
            if x==1:
                m=max(m,key)
        return m