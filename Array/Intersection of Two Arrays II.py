class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for x in nums1:
            if x in nums2:
                a.append(x)
                nums2.remove(x)
        return a