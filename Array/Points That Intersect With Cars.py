class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        a=set()
        for i in nums:
            for j in range(i[0],i[1]+1):
                a.add(j)
        return len(a)