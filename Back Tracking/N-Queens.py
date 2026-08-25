class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid=[['.'for _ in range(n)] for i in range(n)]
        ans=[]
        def safe(r,c):
            for i in range(r+1):
                if grid[i][c]=='Q':
                    return False
            row=r-1
            col=c-1
            while row>=0 and col>=0:
                if grid[row][col]=='Q':
                    return False
                row-=1
                col-=1
            row=r-1
            col=c+1
            while row>=0 and col<n:
                if grid[row][col]=='Q':
                    return False
                row-=1
                col+=1
            return True

        def dfs(row):
            if row==n:
                ans.append(["".join(row) for row in grid])
                return False
            for j in range(n):
                if safe(row,j):
                    grid[row][j]='Q'
                    dfs(row+1)
                    grid[row][j]='.'
        dfs(0)
        return ans