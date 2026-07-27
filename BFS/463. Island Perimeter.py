class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    q.append((i,j))
        t=len(q)*4
        move=[(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c=q.popleft()
            for x,y in move:
                nr=x+r
                nc=y+c
                if nr<0 or nr>=row or nc<0 or nc>=col:
                    continue
                if grid[nr][nc]==1:
                    t-=1
        return t