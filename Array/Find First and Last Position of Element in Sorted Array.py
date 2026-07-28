class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        l=0
        r=len(nums)-1
        x=y=0
        f1=False
        f2=False
        while l<=r:
            if nums[l]==target:
                f2=True
                x=l
            else:
                l+=1
            if nums[r]==target:
                f1=True
                y=r
            else:
                r-=1
            if f1 and f2:
                return [x,y]