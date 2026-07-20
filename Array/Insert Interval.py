class Solution:
    def insert(self, l1: List[List[int]],l2: List[int]) -> List[List[int]]:
        l1.append(l2)
        l1.sort()
        cur=l1[0]
        ans=[]
        for i in range(1,len(l1)):
            if cur[1]>=l1[i][0]:
                cur[1]=max(l1[i][1],cur[1])

            else:
                ans.append(cur)
                cur=l1[i]
        ans.append(cur)
        return ans