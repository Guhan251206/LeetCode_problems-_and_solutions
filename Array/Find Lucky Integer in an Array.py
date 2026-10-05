class Solution:
    def findLucky(self, arr: list[int]) -> int:
        a=[]
        for n in arr:
            if arr.count(n)==n and n not in a:
                a.append(n)
        if not a:
            return -1
        a.sort(reverse=True)
        return a[0]