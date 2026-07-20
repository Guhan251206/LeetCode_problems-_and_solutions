from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c={}
        for i in nums:
            c[i]=c.get(i,0)+1
        k=len(nums)//3
        a=[]
        for i in c:
            if c[i]>k:
                a.append(i)
        return a