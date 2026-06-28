class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        
        if len(a)%2==1:
            return a[len(a)//2]/1
        else:
            n=len(a)//2
            return (a[n]+a[n-1])/2