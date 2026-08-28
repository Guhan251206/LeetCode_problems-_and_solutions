class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        ans=[[-1]*col for ii in range(row)]
        move=[(-1,0),(0,1),(0,-1),(1,0)]
        q=deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    q.append((i,j))
                    ans[i][j]=0
        while q:
            r,c=q.popleft()
            for x,y in move:
                nr=r+x
                nc=c+y
                if nr>=0 and nr<row and nc>=0 and nc<col and ans[nr][nc]==-1:
                    ans[nr][nc]=ans[r][c]+1
                    q.append((nr,nc))
        return ans