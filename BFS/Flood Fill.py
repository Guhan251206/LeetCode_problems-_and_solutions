class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=deque()
        q.append((sr,sc))
        row=len(image)
        col=len(image[0])
        k=image[sr][sc]
        move=[(-1,0),(1,0),(0,-1),(0,1)]
        if k==color:
            return image
        image[sr][sc]=color
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                
                for x,y in move:
                    nr=x+r
                    nc=c+y
                    if nr>=0 and nr<row and nc>=0 and nc<col and image[nr][nc]==k:
                        q.append((nr,nc))
                        image[nr][nc]=color
        return image
