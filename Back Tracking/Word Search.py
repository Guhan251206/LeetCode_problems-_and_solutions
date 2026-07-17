class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        def fun(i,j,inx):
            if inx==len(word):
                return True
            if i<0 or j<0 or i>=row or j>=col or board[i][j]!=word[inx]:
                return False
            t=board[i][j]
            board[i][j]="#"
            ans=(fun(i+1,j,inx+1) or fun(i,j+1,inx+1) or fun(i-1,j,inx+1) or fun(i,j-1,inx+1))
            board[i][j]=t
            return ans
        for i in range(row):
            for j in range(col):
                
                if fun(i,j,0):
                    return True

        return False