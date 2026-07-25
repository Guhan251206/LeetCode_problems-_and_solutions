class Solution:
    def ladderLength(self, start: str, end: str, wo: List[str]) -> int:
        if end not in wo:
            return 0
        d=1
        word=set(wo)
        q=deque()
        q.append((start,d))
        while q:
            cur,d=q.popleft()
            if cur==end:
                return d
            for i in range(len(cur)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if cur[i]==ch:
                        continue
                    s=cur[:i]+ch+cur[i+1:]
                    if s in word:
                        word.remove(s)
                        q.append((s,d+1))          
        return 0