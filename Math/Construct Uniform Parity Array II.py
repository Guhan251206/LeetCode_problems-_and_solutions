class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n=len(nums1)
        even,odd=0,0
        for x in nums1:
            if x%2==0:
                even+=1
            else:
                odd+=1
        if even==n or odd==n:
            return True
        if min(nums1)%2==0:
            return False
        else:
            return True