class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row=len(grid)
        col=len(grid[0])
        move=[(1,0),(-1,0),(0,1),(0,-1)]
        q=deque()
        vist=[[[False]*(k+1) for i in range(col)] for _ in range(row)]
        q.append((0,0,0,k))
        vist[0][0][k]=True
        while q:
            for i in range(len(q)):
                r,c,step,cnt=q.popleft()
                if r==row-1 and c==col-1:
                    return step
                for x,y in move:
                    nr=x+r
                    nc=y+c
                    if nr>=0 and nr<row and nc>=0 and nc<col:
                        if grid[nr][nc]==0:
                            if not vist[nr][nc][cnt]:
                                vist[nr][nc][cnt]=True
                                q.append((nr,nc,step+1,cnt))
                        else:
                            if cnt>0 and not vist[nr][nc][cnt-1]:
                                q.append((nr,nc,step+1,cnt-1))
                                vist[nr][nc][cnt-1]=True
        return -1