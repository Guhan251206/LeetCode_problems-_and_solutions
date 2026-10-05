import heapq

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        pq=[]
        for x in score:
            heapq.heappush(pq,(-x))
        map={}
        rank=0
        while pq:
            val=-heapq.heappop(pq)
            rank+=1
            s=str(rank)
            if rank==1:
                s="Gold Medal"
            elif rank==2:
                s="Silver Medal"
            elif rank==3:
                s="Bronze Medal"
            map[val]=s
        ans=[]
        for x in score:
            ans.append(map[x])
        return ans