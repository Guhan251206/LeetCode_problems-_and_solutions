class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        dead=set(deadends)
        q=deque()
        vist=set()
        start='0000'
        d=0
        q.append((start,d))
        vist.add(start)
        while q:
            cur,d=q.popleft()
            if cur==target:
                return d
            for i in range(4):
                digit=int(cur[i])
                for move in (-1,1):
                    nd=(digit+move)%10
                    s=cur[:i]+str(nd)+cur[i+1:]
                    if s in dead:
                        continue
                    if s not in vist:
                        vist.add(s)
                        q.append((s,d+1))
        return -1