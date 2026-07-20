class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        a=sorted(points,key=lambda x: x[1])
        cur=a[0]
        c=1
        for i in range(1,len(a)):
            if cur[1]<a[i][0]:
                c+=1
            
                cur=a[i]
        print(c)
        return c