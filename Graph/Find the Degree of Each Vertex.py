class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        a=[]
        for x in matrix:
            a.append(sum(x))
        return a