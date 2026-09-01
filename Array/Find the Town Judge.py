class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in trust:
            adj[u-1].append(v-1)
        print(adj)
        ans=-1
        for u in range(n):
            if not adj[u]:
                ans=u
                break
        if ans==-1:
            return -1
        for u in range(n):
            if ans!=u and ans not in adj[u]:
                return -1
        return ans+1