import heapq

class Solution:
    def fillCups(self, amount: list[int]) -> int:
        pq=[]
        for x in amount:
            heapq.heappush(pq,(-x))
        step=0
        while pq:
            x=-heapq.heappop(pq)
            y=-heapq.heappop(pq)
            if x==0 and y==0:
                return step
            if x>0:
                x-=1
            if y>0:
                y-=1
            step+=1
            heapq.heappush(pq,(-x))
            heapq.heappush(pq,(-y))
            
            