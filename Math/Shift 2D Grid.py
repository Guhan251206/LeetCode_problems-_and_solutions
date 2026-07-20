class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        k=k%(row*col)
        dp=[[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                c=(j+k)%col
                r=(i+(j+k)//col)%row
                dp[r][c]=grid[i][j]
        return dp