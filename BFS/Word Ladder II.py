from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, start: str, end: str, wordList: List[str]) -> List[List[str]]:
        word=set(wordList)
        if end not in word:
            return []
        parent=defaultdict(list)
        l={start}
        f=False
        while l and not f:
            word -=l
            used=set()
            for w in l:
                for i in range(len(w)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if w[i]==ch:
                            continue
                        s=w[:i]+ch+w[i+1:]
                        if s in word:
                            used.add(s)
                            parent[s].append(w)
                        if s==end:
                            f=True
            l=used
        if not f:
            return []
        ans=[]
        def dfs(w,path):
            if w==start:
                ans.append(path[:])
                return 
            for child in parent[w]:
                dfs(child,[child]+path)
        dfs(end,[end])
        return ans