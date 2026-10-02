from collections import deque

class Solution:
    def findOrder(self, num: int, arr: list[list[int]]) -> list[int]:
        adj=[[] for _ in range(num)]
        indegree=[0]*num
        for x,y in arr:
            adj[y].append(x)
            indegree[x]+=1
        q=deque()
        for i in range(num):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            u=q.popleft()
            ans.append(u)
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)

        return ans if len(ans)==num else []