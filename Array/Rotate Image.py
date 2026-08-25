class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(a)
        b=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                b[i][j]=a[i][j]
        for i in range(n):
            for j in range(n):    
                a[i][j]=b[n-1-j][i]
           