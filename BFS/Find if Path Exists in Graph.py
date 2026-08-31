from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        vist=[False]*n
        q=deque()
        q.append(source)
        vist[source]=True
        while q:
            u=q.popleft()
            if u==destination:
                return True
            for v in adj[u]:
                if not vist[v]:
                    vist[v]=True
                    q.append(v)
        return False