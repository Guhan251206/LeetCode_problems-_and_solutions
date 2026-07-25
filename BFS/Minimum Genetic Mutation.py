class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        q=deque()
        vist=set()
        d=0
        q.append((start,d))
        vist.add(start)
        while q:
            cur,d=q.popleft()
            if cur==end:
                return d
            for b in bank:
                arr=list(cur)
                for i in range(len(b)):
                    if arr[i]==b[i]:
                        continue
                    t=arr[i]
                    arr[i]=b[i]
                    s="".join(arr)
                    if s in bank and s not in vist:
                        vist.add(s)
                        q.append((s,d+1))
                        break
                    arr[i]=t
                    i+=1
               
        return -1