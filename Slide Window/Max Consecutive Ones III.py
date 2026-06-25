class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z=l=m=0
        for r in range(len(nums)):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            m=max(m,r-l+1)
            
        
        return m