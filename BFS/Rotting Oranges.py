class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        to=0
        q=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    to+=1
                if grid[i][j]==2:
                    q.append((i,j))
        move=[(-1,0),(1,0),(0,-1),(0,1)]
        d=0
        while q and to>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for x,y in move:
                    nr=x+r
                    nc=y+c
                    if nr>=0 and nr<row and nc>=0 and nc<col and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=2
                        to-=1
            d+=1
        if to>0:
            return -1
        else:
            return d
                

        
