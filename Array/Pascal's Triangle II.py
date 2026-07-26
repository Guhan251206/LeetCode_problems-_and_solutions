class Solution:
    def getRow(self, row: int) -> List[int]:
        if row==0:
            return [1]
        a=[]
        for i in range(row+1):
            b=[]
            for j in range(i+1):
                if j==0 or j==i:
                    b.append(1)
                else:
                    b.append(a[i-1][j-1]+a[i-1][j])
            a.append(b)
        return a[row][:]