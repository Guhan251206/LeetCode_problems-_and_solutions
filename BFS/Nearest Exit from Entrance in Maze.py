class Solution:
    def nearestExit(self, maze: List[List[str]], s: List[int]) -> int:
        row=len(maze)
        col=len(maze[0])
        vist=[[False]*col for i in range(row)]
        q=deque()
        q.append((s[0],s[1],0))
        move=[(1,0),(-1,0),(0,1),(0,-1)]
        
        vist[s[0]][s[1]]=True
        while q:
            for i in range(len(q)):
                r,c,step=q.popleft()
                for x,y in move:
                    nr=r+x
                    nc=y+c
                    if nr>=0 and nr<row and nc>=0 and nc<col and maze[nr][nc]=='.' and not vist[nr][nc]:
                        if nr==0 or nr==row-1 or nc==0 or nc==col-1:
                            
                            return step+1
                        vist[nr][nc]=True
                        q.append((nr,nc,step+1))
        return -1