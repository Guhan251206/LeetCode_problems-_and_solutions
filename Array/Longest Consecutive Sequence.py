class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        c=0
        m=1
        l=0
        nums.sort()
        for r in range(1,len(nums)):
            if nums[l]+1==nums[r] :
                c+=1
            elif nums[l]==nums[r]:
                l+=1
                continue
            else:
                c=0
            l+=1
            m=max(m,c+1)
        return m