class Solution:
    def smallestSubsequence(self, s: str) -> str:
        loc={ch:i for i,ch in enumerate(s)}
        stack=[]
        a=set()
        for i,ch in enumerate(s):
            
            if ch in a:
                continue
            while stack and stack[-1]>ch and loc[stack[-1]]>i:
                r=stack.pop()
                a.remove(r)
            stack.append(ch)
            a.add(ch)
        return "".join(stack)