class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        n=8
        sr,sc=source
        sr-=1
        sc-=1
        dr,dc=target
        if sr==dr-1 and sc==dc-1:
            return 0
        elif sc==dc-1:
            r=0
            while  r<n:
                if r==dr-1 and sc==dc-1:
                    return 1
                r+=1
        elif sr==dr-1:
            c=0
            while c<n:
                if sr==dr-1 and c==dc-1:
                    return 1
                c+=1
        else:
            r=sr
            c=sc
            while r>=0 and c>=0:
                if r==dr-1 and c==dc-1:
                    return 1
                r-=1
                c-=1
            r=sr
            c=sc
            while r>=0 and c<n:
                if r==dr-1 and c==dc-1:
                    return 1
                r-=1
                c+=1
            r=sr
            c=sc
            while r<n and c>=0:
                if r==dr-1 and c==dc-1:
                    return 1
                r+=1
                c-=1
            r=sr
            c=sc
            while r<n and c<n:
                if r==dr-1 and c==dc-1:
                    return 1
                r+=1
                c+=1
        return 2