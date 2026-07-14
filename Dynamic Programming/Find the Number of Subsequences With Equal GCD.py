class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        cur=[[0]*201 for _ in range(201)]
        cur[0][0]=1
        ans=0
        mod=10**9+7
        for x in nums:
            g=[[0]*201 for _ in range(201)]
            for g1 in range(201):
                for g2 in range(201):
                    if cur[g1][g2]==0:
                        continue
                    way=cur[g1][g2]
                    g[g1][g2]=(g[g1][g2]+way)%mod
                    ng1=x if g1==0 else gcd(g1,x)
                    g[ng1][g2]=(g[ng1][g2]+way)%mod
                    ng2=x if g2==0 else gcd(g2,x)
                    g[g1][ng2]=(g[g1][ng2]+way)%mod
            cur=g
        for g in range(1,201):
            ans=(ans+cur[g][g])%mod
        return ans