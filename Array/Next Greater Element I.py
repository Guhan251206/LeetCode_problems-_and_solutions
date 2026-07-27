class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for x in nums1:
            f=False
            if x in nums2:
                inx=nums2.index(x)
                if inx<len(nums2)-1:
                    for i in range(inx+1,len(nums2)):
                        if nums2[i]>nums2[inx]:
                            a.append(nums2[i])
                            f=True
                            break
                    if not f:
                        a.append(-1)
                else:
                    a.append(-1)
        return a