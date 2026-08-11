class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        count=0
        vist=[[False]*col for i in range(row)]
        move=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and not vist[i][j]:
                    q.append((i,j))
                    vist[i][j]=True
                    count+=1
                    while q:
                        r,c=q.popleft()
                        for x,y in move:
                            nr=x+r
                            nc=y+c
                            if nr>=0 and nr<row and nc>=0 and nc<col and grid[nr][nc]=='1' and not  vist[nr][nc]:
                                q.append((nr,nc))
                                vist[nr][nc]=True

        return count

