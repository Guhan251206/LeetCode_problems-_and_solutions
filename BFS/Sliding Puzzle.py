class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        row=2
        col=3
        a=''
        q=deque()
        vist=set()
        ans="123450"
        for i in range(row):
            for j in range(col):
               a+=str(board[i][j])
        d=0
        q.append((a,d))
        vist.add(a)
        move=[[1,3],[0,2,4],[1,5],[0,4],[3,1,5],[2,4]]
       
        while q:
                cur,d=q.popleft()
                if(cur==ans):
                    return d
                inx=cur.index('0')
                for i in move[inx]:
                    arr=list(cur)
                    arr[inx],arr[i]=arr[i],arr[inx]
                    s="".join(arr)
                    if s not in vist:
                        vist.add(s) 
                        q.append((s,d+1))

        return -1