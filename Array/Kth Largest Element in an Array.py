    import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq=[]
        for x in nums:
            heapq.heappush(pq,(-x))
        ans=0
        for i in range(k):
            ans=-heapq.heappop(pq)
        return ans