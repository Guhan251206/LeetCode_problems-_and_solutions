class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=0
        for i in range(k):
            s+=arr[i]
        c=0
        if s//k>=threshold:
            c+=1
        l=0
        r=k
        while l<len(arr)-k:
            s-=arr[l]
            s+=arr[r]
            
            if s//k>=threshold:
                c+=1
            l+=1
            r+=1
        return c