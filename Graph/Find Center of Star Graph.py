class Solution:
    def findCenter(self, a: List[List[int]]) -> int:
        n=len(a)+1
        adj=[[] for _ in range(n)]
        for u,v in a:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        print(adj)
        for u in range(n):
            if len(adj[u])==n-1:
                return u+1
        return -1