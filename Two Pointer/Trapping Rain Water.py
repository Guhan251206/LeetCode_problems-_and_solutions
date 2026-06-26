class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        ml=mr=0
        c=0
        while l<r:
            if h[l]<=h[r]:
                ml=max(ml,h[l])
                c+=(ml-h[l])
                l+=1
            else:
                mr=max(mr,h[r])
                c+=(mr-h[r])
                r-=1
        return c