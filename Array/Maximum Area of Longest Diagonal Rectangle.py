import math

class Solution:
    def areaOfMaxDiagonal(self, a: List[List[int]]) -> int:
        arr=[]
        for x,y in a:
            v1=(x*x)+(y*y)
            v2=math.sqrt(v1)
            print(v2,x*y,end=' ')
            arr.append((v2,x*y))
        arr.sort()
        print(arr)
        return arr[-1][1]