class Node:
    def __init__(self):
        self.child={}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Node()
        for w in words:
            node=root
            for ch in w:
                if ch not in node.child:
                    node.child[ch]=Node()
                node=node.child[ch]
            node.word=w
        row=len(board)
        col=len(board[0])
        ans=[]
        def dfs(r,c,node):
            if r<0 or c<0 or r>=row or c>=col:
                return
            ch=board[r][c]
            if ch=="#" or ch not in node.child:
                return
            node=node.child[ch]
            board[r][c]='#'
            if node.word:
                ans.append(node.word)
                node.word=None
            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)
            board[r][c]=ch


        for i in range(row):
            for j in range(col):
                dfs(i,j,root)
        return ans