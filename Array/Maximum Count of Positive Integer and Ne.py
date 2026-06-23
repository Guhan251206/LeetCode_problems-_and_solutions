class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=c1=0
        for i in nums:
            if i<0:
                c+=1
            elif i>0:
                c1+=1
        return max(c,c1)