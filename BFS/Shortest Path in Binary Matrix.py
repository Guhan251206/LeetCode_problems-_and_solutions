class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        move=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        q=deque()
        q.append((0,0,1))
        row=len(grid)
        col=len(grid[0])
        if grid[0][0]==1:
            return -1
        vist=[[False]*col for i in range(row)]
        vist[0][0]=True
        while q:
            for i in range(len(q)):
                r,c,d=q.popleft()
                if r==row-1 and c==col-1:
                    return d
                for x,y in move:
                    nr=x+r
                    nc=y+c
                    if nr>=0 and nr<row and nc>=0 and nc<col and grid[nr][nc]==0 and not vist[nr][nc]:
                        q.append((nr,nc,d+1))
                        vist[nr][nc]=True
        return -1