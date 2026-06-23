class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums:
            if i>0:
                a.append(i)
            elif i<0:
                b.append(i)
        c=[]
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        return c