class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        cur=a[0]
        ans=[]
        for i in range(1,len(a)):
            if cur[1]>=a[i][0]:
                
                cur[1]=max(cur[1],a[i][1])
            else:
                ans.append(cur)
                cur=a[i]
        ans.append(cur)
        return ans