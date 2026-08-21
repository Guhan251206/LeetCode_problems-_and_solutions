class Solution:
    def readBinaryWatch(self, k: int) -> List[str]:
        ans=[]
        for h in range(12):
            for m in range(60):
                hones=bin(h).count('1')
                mones=bin(m).count('1')
                if hones+mones==k:
                    ans.append(f"{h}:{m:02d}")
        return ans