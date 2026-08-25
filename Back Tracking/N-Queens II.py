class Solution:
    def totalNQueens(self, n: int) -> int:
        grid=[['.'for _ in range(n)] for i in range(n)]
        ans=0
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
            nonlocal ans
            if row==n:
                ans+=1
                return False
            for j in range(n):
                if safe(row,j):
                    grid[row][j]='Q'
                    dfs(row+1)
                    grid[row][j]='.'
        dfs(0)
        return ans