class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        MIN=min(nums)
        MAX=max(nums)
        if MIN==MAX:
            return 1
        n=len(nums)
        c=0
        mini=0
        maxi=0
        for i in range(n):
            if nums[i]==MIN:
                mini=i
                c+=1
            elif nums[i]==MAX:
                maxi=i
                c+=1
            if c==2:
                break
        l=min(mini,maxi)
        r=max(mini,maxi)
        front=r+1
        back=n-l
        fb=(l+1)+(n-r)
        return min(front,back,fb)