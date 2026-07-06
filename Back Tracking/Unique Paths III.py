class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ob=n*m
        c=0
        co=0
        s1,s2=0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==-1:
                    c+=1
                if grid[i][j]==1:
                    s1,s2=i,j
                
                
        ob-=c
        s=[[0]*m for _ in range(n)]
        def fi(i,j,step):
            nonlocal co,ob
            if i>=n or i<0 or j<0 or j>=m or grid[i][j]==-1 or s[i][j]==1:
                return 
            if grid[i][j]==2 and step==ob:
                co+=1
                return
            s[i][j]=1
            fi(i+1,j,step+1)
            fi(i,j+1,step+1)
            fi(i-1,j,step+1)
            fi(i,j-1,step+1)
            s[i][j]=0

        fi(s1,s2,1)
        print(co)
        return co