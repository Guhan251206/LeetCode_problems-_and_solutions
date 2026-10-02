from collections import deque

class Solution:
    def canFinish(self, num: int, arr: list[list[int]]) -> bool:
        adj=[[] for _ in range(num)]
        indegree=[0]*num
        for x,y in arr:
            adj[y].append(x)
            indegree[x]+=1
        print(adj)
        q=deque()
        for i in range(num):
            if indegree[i]==0:
                q.append(i)
        vist=0
        while q:
            u=q.popleft()
            vist+=1
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
       
        return num==vist
