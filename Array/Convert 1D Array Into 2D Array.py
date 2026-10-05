class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if n*m!=len(original):
            return []
        ans=[[0]*n for _ in range(m)]
        k=0
        for i in range(m):
            for j in range(n):
                ans[i][j]=original[k]
                k+=1
        return ans