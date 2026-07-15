class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        move=[(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(-1,-2),(1,2),(-1,2)]
        memo={}
        def fun(r,c,k):
            if r<0 or c<0 or r>=n or c>=n:
                return 0
            if k==0:
                return 1
            if (r,c,k) in memo:
                return memo[(r,c,k)]
            ans=0
            for dx,dy in move:
                ans+=fun(r+dx,c+dy,k-1)
            memo[(r,c,k)]=ans
            return ans
        return fun(row,column,k)/(8**k)