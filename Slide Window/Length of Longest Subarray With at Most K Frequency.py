class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        fre={}
        l=0
        best=0
        for r in range(len(nums)):
            fre[nums[r]]=fre.get(nums[r],0)+1
            while fre[nums[r]]>k:
                fre[nums[l]]-=1
                if fre[nums[l]]==0:
                    fre.pop(nums[l])
                l+=1
            best=max(best,r-l+1)
        return best