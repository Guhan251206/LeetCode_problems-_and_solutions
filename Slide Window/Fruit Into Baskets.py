class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a={}
        l=0
        m=0
        for r in fruits:
            s=0
            if r not in a:
                
                if len(a)<2:
                    a[r]=1
                else:
                    while l<len(fruits) and len(a)>1:
                        if a[fruits[l]]==1:
                            del a[fruits[l]]
                        else:
                            a[fruits[l]]-=1
                        l+=1
                    a[r]=1
            else:
                a[r]+=1
            for i in a:
                s+=a[i]
            m=max(m,s)
        return m