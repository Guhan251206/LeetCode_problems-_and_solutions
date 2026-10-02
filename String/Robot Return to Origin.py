class Solution:
    def judgeCircle(self, move: str) -> bool:
        if len(move)%2!=0:
            return False
        d={'L':0,'R':0,'U':0,'D':0}
        for x in move:
            d[x]=d.get(x)+1
        if d['L']!=d['R']:
            return False
        if d['U']!=d['D']:
            return False
        return True