from collections import deque,defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, ls: List[List[int]]) -> List[int]:
        dis=defaultdict(list)
        for x,y in ls:
            dis[x].append(y)
        vist=[0]*n
        
        connect=False

        def bfs(x,s):
            nonlocal connect
            q=deque([s])
            vist[s]=x
            while q:
                node=q.popleft()
                for nxt in dis[node]:
                    if vist[nxt]==1 and x==2:
                        connect=True
                        return
                    if vist[nxt]!=x:
                        vist[nxt]=x
                        q.append(nxt)
        bfs(1,k)
        for i in range(n):
            if i==k or vist[i]==1:
                continue
            bfs(2,i)
        ans=[]
        for i in range(n):
            if not connect and vist[i]==1:
                continue
            ans.append(i)
        return ans