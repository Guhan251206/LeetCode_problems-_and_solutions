class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        map={}
        a=arr.copy()
        a=sorted(set(a))
        c=1
        for i in a:
            
            map[i]=c
            c+=1
        for i in range(len(arr)):
            arr[i]=map[arr[i]]
        return arr